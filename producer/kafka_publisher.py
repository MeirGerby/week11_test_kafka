import json
from confluent_kafka import Producer
from mongo_crud import DBCrud

producer_config = {
    "bootstrap.servers": "localhost:9092"
}

producer = Producer(producer_config)

def delivery_report(err, msg):
    if err:
        print(f"Delivery failed: {err}")
    else:
        print(f"Delivered {msg.value().decode("utf-8")}")

data = DBCrud.get_all_data()
value = json.dumps(data).encode("utf-8")

producer.produce(
    topic="data",
    value=value,
    callback=delivery_report
)

producer.flush(timeout=10.0)
