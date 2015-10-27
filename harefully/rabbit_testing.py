import logging
import multiprocessing as mp
import subprocess

import pika

class CallResponseTestCase(object):
    def __init__(self, message, response):
        self.message = message
        self.response = response

    def apply(self, testing_class):
        testing_class.send_message(self.message)
        input = testing_class.receive_message()
        if input != self.response:
            self.success = False
            return

class ProcessTesting(object):
    messages = []

    def __init__(self, test_cases):
        self.test_cases = test_cases
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters('localhost')
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='keepalive')
        self.channel.queue_purge(queue='keepalive')

    def send_message(self, message):
        self.channel.basic_publish(
            exchange='',
            routing_key='keepalive',
            body=message
        )

    def receive_message(self):
        _, _, body = self.channel.basic_get(queue='keepalive')
        self.messages.append(body)
        
        return self.messages[-1]

    def run_test(self):
        self.p = mp.Process(target=self.function)
        logging.debug("Starting the listener process.")
        self.p.start()
        for a in self.test_cases:
            a.apply(self)
        self.p.join()


