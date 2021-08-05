# START THE KAFKA ENVIRONMENT
## Start the ZooKeeper service
## Note: Soon, ZooKeeper will no longer be required by Apache Kafka.
$ bin/zookeeper-server-start.sh config/zookeeper.properties

## Start the Kafka broker service
$ bin/kafka-server-start.sh config/server.properties

# CREATE A TOPIC TO STORE YOUR EVENTS
$ bin/kafka-topics.sh --create --topic quickstart-events --bootstrap-server localhost:9092

# WRITE SOME EVENTS INTO THE TOPIC
$ bin/kafka-console-producer.sh --topic quickstart-events --bootstrap-server localhost:9092

# READ THE EVENTS
$ bin/kafka-console-consumer.sh --topic quickstart-events --from-beginning --bootstrap-server localhost:9092



git remote add origin https://github.com/bigmario/kafka.git
git branch -M main
git push -u origin main