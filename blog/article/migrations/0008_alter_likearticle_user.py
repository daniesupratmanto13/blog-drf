# Generated by Django 3.2.16 on 2022-12-26 22:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0007_alter_likearticle_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likearticle',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likesuser', to=settings.AUTH_USER_MODEL),
        ),
    ]
