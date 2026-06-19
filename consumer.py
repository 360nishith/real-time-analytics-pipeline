from kafka import KafkaConsumer
import psycopg2
import json

consumer = KafkaConsumer(
    "financial_transactions",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    auto_offset_reset="earliest",
    group_id="fraud-detector"
)

conn = psycopg2.connect(
    host="localhost",
    database="analytics_db",
    user="postgres",
    password="n123@#$100"
)

cursor = conn.cursor()

print("Listening for transactions...")

for message in consumer:

    transaction = message.value

    print("Received:", transaction)

    if transaction["amount"] > 1000:

        print(" ANOMALY DETECTED!")

        cursor.execute(
            """
            INSERT INTO anomalies
            (user_id, amount, transaction_time)
            VALUES (%s, %s, %s)
            """,
            (
                transaction["user_id"],
                transaction["amount"],
                transaction["timestamp"]
            )
        )

        conn.commit()

        print("Saved to PostgreSQL")