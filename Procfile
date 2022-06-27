web: gunicorn appliku_start.wsgi
worker: celery -A appliku_start.celeryapp
release: python manage.py migrate