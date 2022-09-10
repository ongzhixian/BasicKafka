# Running Kafka on Windows


## Step 2: Start the Kafka environment

1.	Start zookeeper
2.	Start kafka broker

``` 
.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
.\bin\windows\kafka-server-start.bat .\config\server.properties

```

## Step 3: Create a topic to store your events

 Kafka is a distributed event streaming platform that lets you read, write, store, and process events 
 (also called records or messages in the documentation) across many machines.

Example events are payment transactions, geolocation updates from mobile phones, shipping orders, sensor measurements from IoT devices or medical equipment, and much more. 
These events are organized and stored in topics. 
Very simplified, a topic is similar to a folder in a filesystem, and the events are the files in that folder. 

So before you can write your first events, you must create a topic. Open another terminal session and run: 

```
.\bin\windows\kafka-topics.bat --create --topic quickstart-events --bootstrap-server localhost:9092
.\bin\windows\kafka-topics.bat --describe --topic quickstart-events --bootstrap-server localhost:9092
```

## Step 4: Write some events into the topic

 A Kafka client communicates with the Kafka brokers via the network for writing (or reading) events. 
 Once received, the brokers will store the events in a durable and fault-tolerant manner for as long as you need—even forever.

Run the console producer client to write a few events into your topic. 
By default, each line you enter will result in a separate event being written to the topic. 

```
.\bin\windows\kafka-console-producer.bat --topic quickstart-events --bootstrap-server localhost:9092
```

## Step 5: Read the events

.\bin\windows\kafka-console-consumer.bat --topic quickstart-events --from-beginning --bootstrap-server localhost:9092


## Step 6: Import/export your data as streams of events with Kafka Connect



# Reference

https://kafka.apache.org/quickstart
