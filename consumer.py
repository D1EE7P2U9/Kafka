
from kafka import KafkaConsumer
consumer = KafkaConsumer(
    'dee',
    bootstrap_servers=['localhost:9092', 'localhost:9093', 'localhost:9094'],
    group_id='dee-consumer-group'
)

for message in consumer:
    print(message)
