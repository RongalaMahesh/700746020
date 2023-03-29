import boto3
import configparser


def create_queue(mahesh):
    sqs = boto3.resource('sqs')
    queue = sqs.create_queue(QueueName=mahesh)
    return queue.url


def send_message_to_queue(queue_url, message_body):
    sqs = boto3.client('sqs')
    sqs.send_message(QueueUrl=queue_url, MessageBody=message_body)


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('mahesh.ini')

    mahesh = config['mahesh']
    queue_url = create_queue(mahesh)



