from confluent_kafka import Producer
import socket

def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))


if __name__ == "__main__":

    conf = {
        'bootstrap.servers': "localhost:9092,localhost:9092",
        'client.id': socket.gethostname()
    }

    producer = Producer(conf)

    ## Asynchronous writes
    # producer.produce(topic, key="key", value="value")
    # OR
    producer.produce(topic, key="key", value="value", callback=acked)

    # Wait up to 1 second for events. Callbacks will be invoked during
    # this method call if the message is acknowledged.
    producer.poll(1)

    # Synchronous writes
    # producer.produce(topic, key="key", value="value")
    # producer.flush()