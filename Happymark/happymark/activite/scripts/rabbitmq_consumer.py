# activite/scripts/rabbitmq_consumer.py

def run():
    start_consuming()

def start_consuming():
    import pika
    import json
    from activite.models import Activite, Sponsor

    def callback(ch, method, properties, body):
        sponsor_data = json.loads(body)
        sponsor, created = Sponsor.objects.get_or_create(
            id=sponsor_data['id'],
            defaults={
                'name': sponsor_data['name'],
                'description': sponsor_data['description'],
                'created_at': sponsor_data['created_at']
            }
        )

        # Logique pour lier le sponsor à l'activité

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='sponsor_created')
    channel.basic_consume(queue='sponsor_created', on_message_callback=callback, auto_ack=True)

    channel.start_consuming()
