import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from .models import ChatMessage

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.receiver_id = self.scope['url_route']['kwargs']['receiver_id']
        await self.accept()
        print(f"WebSocket connected for receiver_id: {self.receiver_id}")

    async def disconnect(self, close_code):
        print(f"WebSocket disconnected for receiver_id: {self.receiver_id}")

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender_id = text_data_json['sender_id']
        receiver_id = text_data_json['receiver_id']
        sender_username = text_data_json['sender_username']

        print(f"Received message: {message} from sender_id: {sender_id} to receiver_id: {receiver_id}")

        # Save message to database
        await self.save_message(sender_id, receiver_id, message)

        # Broadcast message to both sender and receiver
        await self.send(text_data=json.dumps({
            'message': message,
            'sender_id': sender_id,
            'sender_username': sender_username
        }))

    async def save_message(self, sender_id, receiver_id, message):
        sender = await User.objects.aget(id=sender_id)
        receiver = await User.objects.aget(id=receiver_id)
        await ChatMessage.objects.acreate(sender=sender, receiver=receiver, message=message)
        print(f"Message saved: {message} from {sender.username} to {receiver.username}")