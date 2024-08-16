from django.urls import path
from comments.consumers import CommentConsumer
from djangochannelsrestframework.consumers import view_as_consumer

websocket_urlpatterns = [
    path("ws/comments/", view_as_consumer(CommentConsumer.as_asgi())),
]
