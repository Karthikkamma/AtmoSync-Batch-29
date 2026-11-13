

import os
from pathlib import Path
from getpass import getpass

import snowflake.connector
from dotenv import load_dotenv
from cryptography.hazmat.primitives import serialization

load_dotenv()

key_path = Path.home() / ".snowflake" / "keys" / "rsa_key.p8"

passphrase = getpass("Enter your private-key passphrase: ")

with open(key_path, "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=passphrase.encode()
    )

connection = None

try:
    connection = snowflake.connector.connect(
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        user=os.getenv("SNOWFLAKE_USER"),
        private_key=private_key,
        role=os.getenv("SNOWFLAKE_ROLE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA"),
    )

    cursor = connection.cursor()
    try:
        cursor.execute("SELECT CURRENT_VERSION()")
        print("Snowflake connection successful!")
        print("Snowflake version:", cursor.fetchone()[0])
    finally:
        cursor.close()

except Exception as error:
    print("Snowflake connection failed.")
    print("Error:", error)

finally:
    if connection is not None:
        connection.close()
