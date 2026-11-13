
import json
import os
from pathlib import Path
from getpass import getpass

from kafka import KafkaConsumer
import snowflake.connector
from dotenv import load_dotenv
from cryptography.hazmat.primitives import serialization

load_dotenv()

# Load the Snowflake private key
key_path = Path.home() / ".snowflake" / "keys" / "rsa_key.p8"
passphrase = getpass("Enter your Snowflake private-key passphrase: ")

with open(key_path, "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=passphrase.encode()
    )

# Connect to Snowflake before reading Kafka messages
connection = snowflake.connector.connect(
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    user=os.getenv("SNOWFLAKE_USER"),
    private_key=private_key,
    role=os.getenv("SNOWFLAKE_ROLE"),
    database=os.getenv("SNOWFLAKE_DATABASE"),
    schema=os.getenv("SNOWFLAKE_SCHEMA"),
)

# Prepare the INSERT statement
insert_sql = """
INSERT INTO ATMOSYNC_DB.RAW.CONTAINER_TELEMETRY (
    CONTAINER_ID,
    EVENT_TIMESTAMP,
    TEMPERATURE_C,
    HUMIDITY_PERCENT,
    LATITUDE,
    LONGITUDE,
    IS_SIMULATED
)
SELECT
    %s,
    TO_TIMESTAMP_TZ(%s),
    %s,
    %s,
    %s,
    %s,
    %s
"""

consumer = None
cursor = None

try:
    cursor = connection.cursor()

    consumer = KafkaConsumer(
        "atmosync-telemetry",
        bootstrap_servers="localhost:9092",
        auto_offset_reset="earliest",
        enable_auto_commit=False,
        group_id="atmosync-snowflake-ingestion",
        consumer_timeout_ms=10000,
        value_deserializer=lambda value: json.loads(
            value.decode("utf-8")
        ),
    )

    print("Connected to Kafka and Snowflake.")

    for message in consumer:
        data = message.value

        values = (
            data["container_id"],
            data["timestamp"],
            data["temperature_c"],
            data["humidity_percent"],
            data["latitude"],
            data["longitude"],
            data["simulated"],
        )

        cursor.execute(insert_sql, values)
        connection.commit()

        # Commit the Kafka offset only after Snowflake succeeds
        consumer.commit()

        print("Inserted telemetry:", data["container_id"])

finally:
    if consumer is not None:
        consumer.close()
    if cursor is not None:
        cursor.close()
    connection.close()

print("Kafka to Snowflake ingestion completed.")

