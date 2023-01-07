from django.utils.text import slugify
from uuid import uuid4


def get_random_code():
    return str(uuid4())[:8].replace('-', '').lower()


def unique_slugify(title, temp_title, slug, Model):

    temp_slug = slug

    if title != temp_title or slug == "":
        temp_slug = slugify(
            str(title))
        exists_slug = Model.objects.filter(slug=temp_slug).exists()
        while exists_slug:
            temp_slug = slugify(temp_slug + ' ' + get_random_code())
            exists_slug = Model.objects.filter(
                slug=temp_slug).exists()

    return temp_slug
