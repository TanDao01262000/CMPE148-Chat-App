# chat/consumers.py
import json

from django.contrib.auth.models import User
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Room, Message
import re
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        sanitized_room_name = re.sub(r'\W+', '', self.room_name)
        self.room_group_name = f"chat_{sanitized_room_name}"
        print(f"Connecting to room: {self.room_name}")
       
        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()
        print(f"Accepted connection to room: {self.room_name}")

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
     

        await self.save_message(username,  message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))


    @sync_to_async
    def save_message(self, username, message):
        user = User.objects.get(username=username)
        room = Room.objects.get(name=self.room_name)
        Message.objects.create(user=user, room=room, content=message)
        print(f"Saved message in room: {room}")