from confluent_kafka import Producer
import json


with open("./clients.json", "r") as f:
    data = json.load(f)
 
p = Producer({'bootstrap.servers': 'localhost:9092'})
p.produce('quickstart-events', key='hello', value=json.dumps(data))
p.flush(30)