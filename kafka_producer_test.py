from kafka import KafkaProducer
from kafka.errors import KafkaError

# setup producer to connect to default server + port
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

# send some message in byte format
future = producer.send('my-topic', value=b'Some message')

# Block for 'synchronous' sends
try:
    record_metadata = future.get(timeout=10)

    # Successful result returns metadata
    print(record_metadata)

except KafkaError:
    # Decide what to do if produce request failed...
    print("Exception occurred")
    pass
