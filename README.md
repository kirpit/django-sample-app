django-sample-app
=================

Install requirements within your virtualenv:
`pip install -r requirements.txt`

Remember to install readline with easy_install for shell_plus:
`easy_install -a readline`

Create the symbolic link to your django admin static files under "media" dir:
`ln -s /path/to/site-packages/django/contrib/admin/static/admin /path/to/project/media/admin`

Go to [http://www.miniwebtool.com/django-secret-key-generator/](http://www.miniwebtool.com/django-secret-key-generator/), create your secret key, copy it. Edit your `sampleapp/settings/default.py`, find `SECRET_KEY` line, paste your secret key.

Copy `sampleapp/settings/local.template.py` => local.py into the same directory and modify necessary changes.

Do `./manage.py syncdb` and `./manage.py migrate`

Ready?
