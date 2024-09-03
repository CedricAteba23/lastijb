# main_app/rabbitmq.py
import pika
import json
from .models import Activite

def consume_sponsor():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='sponsor_queue')

    def callback(ch, method, properties, body):
        sponsor_data = json.loads(body)
        # Mettez à jour ou créez une activité avec le sponsor_id
        activity = Activite.objects.filter(sponsor_id=sponsor_data['id']).first()
        if activity:
            activity.sponsor_id = sponsor_data['id']
            activity.save()

    channel.basic_consume(queue='sponsor_queue',
                          on_message_callback=callback,
                          auto_ack=True)

    print('Waiting for sponsor messages...')
    channel.start_consuming()

# Exécutez cette fonction dans un processus séparé ou un worker