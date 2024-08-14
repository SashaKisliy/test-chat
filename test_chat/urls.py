from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from comments.views import CommentViewSet

router = DefaultRouter()
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('comments.urls')),
]