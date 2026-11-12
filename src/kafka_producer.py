
from pathlib import Path
import json
from kafka import KafkaProducer

PROJECT_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_DIR / "dataset" / "processed" / "price_records.jsonl"

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda value: json.dumps(value).encode("utf-8")
)

count = 0

with INPUT_FILE.open("r", encoding="utf-8") as file:
    for line in file:
        record = json.loads(line)
        producer.send("atmosync-prices", value=record)
        count += 1

producer.flush()
producer.close()

print("Kafka publishing completed.")
print("Records sent:", count)
