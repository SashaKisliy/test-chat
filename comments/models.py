from django.db import models

from user.models import User

from PIL import Image


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="comments/images/", null=True, blank=True)
    text_file = models.FileField(upload_to="comments/texts/", null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image)
            img.thumbnail((320, 240))
            img.save(self.image.path)
