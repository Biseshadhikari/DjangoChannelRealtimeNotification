# consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class FriendRequestConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.username = self.scope['user'].username
        self.room_group_name = f"friendreq_{self.username}"
        print(self.room_group_name)

        # Add the user to their specific group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Remove the user from the group when the WebSocket closes
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        target_username = data['username']

        # Check if the target user is connected and send the message
        await self.channel_layer.group_send(
            f"friendreq_{target_username}",
            {
                'type': 'chat.message',
                'message': message,
                'username': self.username,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        # Send the message to the WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))
