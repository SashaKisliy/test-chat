from django.urls import path
from djangochannelsrestframework.consumers import view_as_consumer
from .consumers import CommentConsumer

urlpatterns = []

websocket_urlpatterns = [
    path('ws/comments/', view_as_consumer(CommentConsumer.as_asgi())),
]