
import json
import random
import time
from datetime import datetime, timezone

from kafka import KafkaProducer

TOPIC = "atmosync-telemetry"

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda value: json.dumps(value).encode("utf-8"),
)

# Example refrigerated container locations (simulated).
containers = [
    {"id": "CONT-001", "lat": 17.6868, "lon": 83.2185},
    {"id": "CONT-002", "lat": 16.5062, "lon": 80.6480},
    {"id": "CONT-003", "lat": 17.3850, "lon": 78.4867},
]

for cycle in range(5):
    for container in containers:
        reading = {
            "container_id": container["id"],
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "temperature_c": round(random.uniform(2, 12), 2),
            "humidity_percent": round(random.uniform(65, 95), 2),
            "latitude": container["lat"],
            "longitude": container["lon"],
            "simulated": True,
        }

        producer.send(TOPIC, value=reading)
        print(json.dumps(reading))

    time.sleep(1)

producer.flush()
producer.close()

print("Successfully published 15 simulated IoT readings to Kafka.")
