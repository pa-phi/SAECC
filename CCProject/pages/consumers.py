import json
from random import randint 
from time import sleep 

from channels.generic.websocket import WebsocketConsumer


class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        self.send(json.dumps({'message': randint(1,100)}))

