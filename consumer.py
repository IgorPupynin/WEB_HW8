import pika
from mongoengine import connect
from model import Contact


connect(db='web10', host="mongodb+srv://userweb10:567234@sandbox.n44nvce.mongodb.net/web10?retryWrites=true&w=majority")


def process_message(channel, method, properties, body):
    contact_id = body.decode()
    contact = Contact.objects(id=contact_id, is_sent=False).first()
    if contact:
        send_email(contact)
        contact.is_sent = True
        contact.save()
        print(f"Сообщение отправлено контакту {contact.fullname}")

    channel.basic_ack(delivery_tag=method.delivery_tag)


def send_email(contact):
    print(f"Отправка сообщения на email {contact.email}")


if __name__ == '__main__':
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='email_queue')

    channel.basic_qos(prefetch_count=1)

    channel.basic_consume(queue='email_queue', on_message_callback=process_message)

    print("Ожидание сообщений...")

    channel.start_consuming()
