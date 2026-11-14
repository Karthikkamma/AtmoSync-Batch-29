
import json
import os
from pathlib import Path
from getpass import getpass

import snowflake.connector
from dotenv import load_dotenv
from cryptography.hazmat.primitives import serialization

load_dotenv()

# Locate the dataset relative to the project folder.
dataset_path = (
    Path(__file__).resolve().parent.parent
    / "dataset"
    / "processed"
    / "price_records.jsonl"
)

# Load the Snowflake RSA private key.
key_path = Path.home() / ".snowflake" / "keys" / "rsa_key.p8"
passphrase = getpass("Enter your Snowflake private-key passphrase: ")

with open(key_path, "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=passphrase.encode()
    )

connection = snowflake.connector.connect(
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    user=os.getenv("SNOWFLAKE_USER"),
    private_key=private_key,
    role=os.getenv("SNOWFLAKE_ROLE"),
    database=os.getenv("SNOWFLAKE_DATABASE"),
    schema=os.getenv("SNOWFLAKE_SCHEMA"),
)

try:
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT COUNT(*) FROM ATMOSYNC_DB.RAW.AGRICULTURAL_PRICES"
        )
        existing_count = cursor.fetchone()[0]

        if existing_count != 0:
            print(
                f"Table already has {existing_count} records. "
                "Skipping import to prevent duplicates."
            )
        else:
            with open(dataset_path, "r", encoding="utf-8") as file:
                records = [
                    (json.dumps(json.loads(line)),)
                    for line in file
                    if line.strip()
                ]

            print(f"Loaded {len(records)} records from JSONL.")

            insert_sql = """
                INSERT INTO ATMOSYNC_DB.RAW.AGRICULTURAL_PRICES (RECORD)
                SELECT PARSE_JSON(%s)
            """

            for record in records:
                cursor.execute(insert_sql, record)

            connection.commit()

            print(f"Inserted {len(records)} agricultural price records.")


finally:
    connection.close()
