from confluent_kafka import Producer

def acked(err, msg):
    if err is not None:
        print(f"Failed to deliver message: {msg.value()}: {err.str()}")
    else:
        print(f"Message produced: {msg.value()}")

p = Producer({'bootstrap.servers': 'localhost:9092'})

try:
    for val in range(1, 1000):
        p.produce('quickstart-events', f'myvalue #{val}', callback=acked)
        p.poll(0.5)

except KeyboardInterrupt:
    pass

p.flush(30)
