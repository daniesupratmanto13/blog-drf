# Generated by Django 3.2.16 on 2022-12-27 01:17

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0009_alter_likearticle_article'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LikeArticle',
            new_name='LikeUnlikeArticle',
        ),
    ]
