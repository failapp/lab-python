import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.0.201', port=5672))

channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='publicacion test .. !')

print(" [x] publicacion test .. !! ")

connection.close()
