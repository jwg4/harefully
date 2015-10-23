import simplejson as json

import pika

def respond(channel, _1, _2, _3, message):    
    try:
        data = json.loads(message)
        if 'token' in data and 'syn' in data:
            payload = {'ack': 1, 'token': data['token']}
            routing_key = 'keepalive'
        else:
            payload = {'error': 1, 'received': data}
            routing_key = 'error'
    except:
        payload = {'error': 1, 'received': json.dumps(message)}
        routing_key = 'error'

    channel.basic_publish(
        exchange='',
        routing_key=routing_key,
        body=json.dumps(payload)
    )

if __name__ == '__main__':
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost')
    )
    channel = connection.channel()
    channel.queue_declare(queue='keepalive')
    fn = lambda w, x, y, z: respond(channel, w, x, y, z)
    channel.basic_consume(
        fn,
        queue='keepalive',
        no_ack=True
    )                  
    channel.start_consuming()
