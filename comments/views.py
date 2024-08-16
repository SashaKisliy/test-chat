from rest_framework import viewsets
from .models import Comment
from .serializers import CommentSerializer


from rest_framework.pagination import PageNumberPagination


class CommentPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = "page_size"
    max_page_size = 100


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("-created_at")
    serializer_class = CommentSerializer
    pagination_class = CommentPagination
    filterset_fields = ["author__username", "created_at"]
