import pika
import json

def rMQ_send(id, message):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='математика')

    data = {
        "id": id,
        "message": message
    }
    message = json.dumps(data)

    channel.basic_publish(exchange='', routing_key='математика', body=message)
    print(f" [x] Sent {message}")

    connection.close()

def rMQ_get_specific_message(id):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')

    method_frame, header_frame, body = channel.basic_get(queue='hello', no_ack=True)
    while body:
        data = json.loads(body)
        if data.get('id') == id:
            print(f" [x] Received id: {data['id']}, message: {data['message']}")
            break
        method_frame, header_frame, body = channel.basic_get(queue='hello', no_ack=True)

    connection.close()


rMQ_send(222, 'попытка 3')
# rMQ_get_specific_message
# Пример получения конкретного сообщения по id
# rMQ_get_specific_message(222)


# import asyncio
# import aiormq
#
# async def rMQ_send():
#     conn = await aiormq.connect('amqp://guest:guest@localhost/')
#     channel = await conn.channel(publisher_confirms=True)
#
#     await channel.basic_publish('тут сообщение', routing_key='РоутингКей')
#     print('[x]')
#
# rMQ_send()