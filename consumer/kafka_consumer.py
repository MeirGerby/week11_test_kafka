import json

from confluent_kafka import Consumer
from mysql_connection import connection

consumer_config = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "analytics-service",
    "auto.offset.reset": "earliest"
}

consumer = Consumer(consumer_config)

consumer.subscribe(["data"])

print("Consumer is running and subscribed to orders topic")

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print(" Error:", msg.error())
            continue

        value = msg.value().decode("utf-8")
        data = json.loads(value)

        print(f"Received order: {data['quantity']} x {data['item']} from {data['user']}")
except KeyboardInterrupt:
    print("\n Stopping consumer")

finally:
    consumer.close()


    