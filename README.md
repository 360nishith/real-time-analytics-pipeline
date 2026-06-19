# Real-Time Analytics Pipeline

A simple real-time analytics project built with:

- Python
- Apache Kafka
- PostgreSQL
- Docker

## Architecture

```text
Producer
   ↓
Kafka Topic
(financial_transactions)
   ↓
Consumer
   ↓
PostgreSQL
```

## Components

### Producer
Generates transaction events and sends them to Kafka.

### Kafka
Acts as the message broker.

### Consumer
Reads transaction events from Kafka and detects anomalies.

### PostgreSQL
Stores suspicious transactions for further analysis.

## Project Structure

```text
real-time-analytics-pipeline/
│
├── docker-compose.yml
├── producer.py
├── consumer.py
├── requirements.txt
└── README.md
```