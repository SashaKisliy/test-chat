import bleach
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    file = serializers.FileField(required=False)

    class Meta:
        model = Comment
        fields = ["author", "text", "created_at", "image", "file"]

    def create(self, validated_data):
        if "user" in validated_data:
            validated_data["author"] = validated_data.pop("user")
        validated_data["text"] = bleach.clean(
            validated_data["text"], tags=["a", "code", "i", "strong"]
        )
        return super().create(validated_data)
