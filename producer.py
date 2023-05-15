import pika
from mongoengine import connect
from model import Contact


connect(db='web10', host="mongodb+srv://userweb10:567234@sandbox.n44nvce.mongodb.net/web10?retryWrites=true&w=majority")


NUM_CONTACTS = 10

if __name__ == '__main__':
    for _ in range(NUM_CONTACTS):
        fullname = f"Имя{_}"
        email = f"email{_}@example.com"
        additional_info = f"Дополнительная информация для контакта {_}"
        contact = Contact(fullname=fullname, email=email, additional_info=additional_info)
        contact.save()

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='email_queue')

    for contact in Contact.objects():
        message = str(contact.id)
        channel.basic_publish(exchange='', routing_key='email_queue', body=message)
        print(f"Сообщение для контакта {contact.fullname} отправлено в очередь")

    connection.close()
