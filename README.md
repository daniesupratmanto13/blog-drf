# django, drf
## blog app
## with auth token

Clone:

```sh
git@github.com:daniesupratmanto13/blog-drf.git
cd blog-drf
```

Install it and run:

```sh
pipenv install
pipenv shell
cd blog
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```