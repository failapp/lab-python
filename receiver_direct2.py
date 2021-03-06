import pika

#connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.0.201', port=5672))

credentials = pika.PlainCredentials('admin', 'architeq2020.')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='amqp.architeq.cl', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='besalco', exchange_type='direct')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

# se pueden enlazar varios canales directos 'route keys' ..
route_key = 'cas.device.00:17:61:10:2A:A4'
channel.queue_bind(exchange='besalco', queue=queue_name, routing_key=route_key)


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))



print(' [*] Waiting for logs. To exit press CTRL+C')
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()
