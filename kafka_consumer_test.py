from kafka import KafkaConsumer

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer(
    'my-topic',
    bootstrap_servers=['localhost:9092']
)

# message value and key are raw bytes -- decode if necessary!
for message in consumer:
    print("Entire message: ", message)
    print("")
    print(
        "%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                       message.offset, message.key,
                                       message.value)
    )
    print("")
