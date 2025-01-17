# chat_app/routing.py

from django.urls import re_path
from chat import consumers  # Import your WebSocket consumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_id>\w+)/$', consumers.ChatConsumer.as_asgi()),
]