django-sample-app
=================

Install requirements within your virtualenv:
`pip install -r requirements.txt`

Remember to install readline with easy_install for shell_plus:
`easy_install -a readline`

Create the symbolic link to your django admin static files under "media" dir:
`ln -s /path/to/site-packages/django/contrib/admin/static/admin /path/to/project/media/admin`

Copy local.template.py => local.py and modify necessary changes.

Do `./manage.py syncdb` and `./manage.py migrate`

Ready?