from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import ListModelMixin, CreateModelMixin
from .models import Comment
from .serializers import CommentSerializer


class CommentConsumer(ListModelMixin, CreateModelMixin, GenericAsyncAPIConsumer):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
