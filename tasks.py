from celery import Celery
from pymongo import MongoClient
import pika
import json

# RabbitMQ


# MongoDB
client = MongoClient('localhost', 27017)
db_connection = client.celery
collection = db_connection['tasks']

app = Celery('tasks', backend='amqp', broker='amqp://')

@app.task()
def insert_task(task_id):
    collection.insert({'task_id': task_id})
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.basic_publish(exchange='celery_out',
                          routing_key='outgoing',
                          body=json.dumps({'task_id': task_id}))
    channel.close()