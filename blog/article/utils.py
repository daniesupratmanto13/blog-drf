import os
from django.conf import settings
from django.utils.text import slugify
from uuid import uuid4


def get_random_code(n: int) -> str:

    return str(uuid4())[:n].replace("-", "").upper()


def unique_slugify(title, temp_title, slug, Model, len_random: int) -> str:

    temp_slug = slug

    if title != temp_title or slug == "":
        temp_slug = slugify(
            str(title))
        exists_slug = Model.objects.filter(slug=temp_slug).exists()
        while exists_slug:
            temp_slug = slugify(temp_slug + ' ' + get_random_code(len_random))
            exists_slug = Model.objects.filter(
                slug=temp_slug).exists()

    return temp_slug


def profile_pic_path(instance, filename):

    profile_pic_name = f'profile_pics/user_{instance.user.id}_{instance.user.username}/profile_{filename}'
    full_path = os.path.join(settings.MEDIA_ROOT, profile_pic_name)

    if os.path.exists(full_path):
        os.remove(full_path)

    return profile_pic_name
