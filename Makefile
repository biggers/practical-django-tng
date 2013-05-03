# NOTE: must use real tabs, not spaces, in a Makefile!
 Just remember that you need to use real tabs, not spaces, in a Makefile

.PHONY: testrun
run: bin/django syncdb compile_trans
	./bin/django runserver 0.0.0.0:8000

.PHONY: werkzeug
werkzeug: bin/django syncdb
        ./bin/django runserver_plus

# requires uWSGI >= 1.2
.PHONY: uwsgi
uwsgi: # bin/django syncdb
        uwsgi --ini deploy/uwsgi.ini --py-autoreload=3

.PHONY: shell_plus
shell_plus: bin/django syncdb
        ./bin/django shell_plus

bin/django: bin/buildout  buildout.cfg
        script -c "./bin/buildout -N" build.$$.log  && touch bin/django

bin/buildout:
        python bootstrap.py --distribute

syncdb: bin/django
        ./bin/django syncdb --noinput && touch syncdb

project/locale:
        mkdir project/locale

.PHONY: make_trans
trans: bin/django project/locale
        find project -name '*.haml_trans' -delete
        find project -name '*.haml' -exec bin/hamlpy {} {}_trans \;
        ./bin/django makemessages -a -e 'py,html,haml_trans,txt' -i 'django-payokay' -i docs -i django-guardian
        ./bin/django makemessages -d djangojs -a -i project/static/CACHE
        find project -name '*.haml_trans' -delete

compile_trans:
        find project/locale/ -mindepth 1 -maxdepth 1 -type d -exec make {}/LC_MESSAGES/django.mo {}/LC_MESSAGES/djangojs.mo \;
