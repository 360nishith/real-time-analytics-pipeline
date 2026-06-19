from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "financial_transactions",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    auto_offset_reset="earliest",
    group_id="fraud-detector"
)

print("Listening for transactions...")

for message in consumer:
    transaction = message.value

    print("Received:", transaction)

    if transaction["amount"] > 1000:
        print("ANOMALY DETECTED!")