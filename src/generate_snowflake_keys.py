
from pathlib import Path
from getpass import getpass

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

folder = Path.home() / ".snowflake" / "keys"
folder.mkdir(parents=True, exist_ok=True)

private_path = folder / "rsa_key.p8"
public_path = folder / "rsa_key.pub"

if private_path.exists() or public_path.exists():
    print("Key file already exists. No files were overwritten.")
else:
    password = getpass("Create a NEW private-key passphrase: ")

    if not password:
        raise ValueError("Passphrase cannot be empty.")

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    private_path.write_bytes(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(
                password.encode()
            )
        )
    )

    public_path.write_bytes(
        private_key.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    )

    print("Snowflake key pair generated successfully!")
