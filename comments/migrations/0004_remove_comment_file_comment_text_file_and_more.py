# Generated by Django 5.1 on 2024-08-16 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("comments", "0003_comment_file_comment_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="file",
        ),
        migrations.AddField(
            model_name="comment",
            name="text_file",
            field=models.FileField(blank=True, null=True, upload_to="comments/texts/"),
        ),
        migrations.AlterField(
            model_name="comment",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="comments/images/"
            ),
        ),
    ]
