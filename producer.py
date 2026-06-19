from kafka import KafkaProducer
from faker import Faker
from datetime import datetime
import json
import random
import time

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

fake = Faker()

TOPIC = "financial_transactions"

while True:

    transaction = {
        "user_id": random.randint(100, 999),
        "amount": round(random.uniform(10, 5000), 2),
        "timestamp": datetime.now().isoformat()
    }

    producer.send(TOPIC, transaction)
    producer.flush()

    print("Sent:", transaction)

    time.sleep(2)