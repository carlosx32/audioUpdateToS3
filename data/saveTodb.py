from Kafka import KafkaConsumer
import os

consumer = KafkaConsumer(os.environ['AUDIO_UPLOAD_EVENT'],
                         group_id=os.environ['GROUP_ID'],
                         bootstrap_servers=[os.environ['KAFKA_SERVER']],
                         auto_offset_reset='earliest')
for message in consumer:
    print("mensaje",message)