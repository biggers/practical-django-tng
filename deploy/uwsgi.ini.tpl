[uwsgi]
plugins = python
socket = ${uwsgi:connection}
master = true
processes = 4
wsgi-file = bin/django.wsgi
