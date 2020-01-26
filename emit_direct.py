import pika

#connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.0.201', port=5672))

credentials = pika.PlainCredentials('admin', 'architeq2020.')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='amqp.architeq.cl', port=5672, credentials=credentials))
channel = connection.channel()

#channel.exchange_declare(exchange='direct_logs', exchange_type='direct')
channel.exchange_declare(exchange='besalco', exchange_type='direct')

#route_key = 'info'
route_key = 'cas.device.00:17:61:10:2A:A4'
message = 'Mensaje canal directo ..'

#channel.basic_publish(exchange='direct_logs', routing_key=route_key, body=message)
channel.basic_publish(exchange='besalco', routing_key=route_key, body=message)

print(" [x] Sent %r:%r" % (route_key, message))
connection.close()