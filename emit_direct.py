import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.0.201', port=5672))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

route_key = 'info'
message = 'Mensaje canal directo ..'

channel.basic_publish(exchange='direct_logs', routing_key=route_key, body=message)

print(" [x] Sent %r:%r" % (route_key, message))
connection.close()