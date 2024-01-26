from django.urls import path
from . import consumers

websocket_patterns = [
    path('ws/connect/', consumers.FriendRequestConsumer.as_asgi()),
]