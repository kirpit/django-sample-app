# django-sample-app

django-sample-app is a **minimal** sample application to start developing your web project immediately on [Django framework](https://www.djangoproject.com/). 

The sample application comes with:

* [html5shiv](https://github.com/afarkas/html5shiv)
* [jQuery](http://jquery.com/) v2.1.0 (No support for IE-8 or below)
* [Twitter Bootstrap](http://getbootstrap.com/) v3.3.5
* [Font Awesome](http://fontawesome.io/) v4.3.0

that are glued together with [initializr](http://www.initializr.com/). And its current `requirements.txt` file is:

```
Django==1.8.2
django-compressor==1.5
django-debug-toolbar==1.3.2
django-extensions==1.5.5
ipython==3.2.0
psycopg2==2.6.1
six==1.9.0
sqlparse==0.1.15
wsgiref==0.1.2
```

## Installation

### 1. virtualenv / virtualenvwrapper
You should already know what is [virtualenv](http://www.virtualenv.org/), preferably [virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/) at this stage. So, simply create it for your own project, where `projectname` is the name of your project:

`$ mkvirtualenv --clear projectname`

### 2. Download
Now, you need the *django-sample-app* project files in your workspace:

    $ cd /path/to/your/workspace
    $ git clone git://github.com/kirpit/django-sample-app.git projectname && cd projectname

### 3. Requirements
Right there, you will find the *requirements.txt* file that has all the great debugging tools, django helpers and some other cool stuff. To install them, simply type:

`$ pip install -r requirements.txt`

### 4. Tweaks

#### wsgi.py
`projectname/wsgi.py` file is necessary for WSGI gateways (such as uWSGI) to run your Django application and also required from Django itself. You definitely want to change `{{ project_name }}` value in this file to whatever you name your application (e.g. `bookstore.settings`).

#### SECRET_KEY
Go to <http://www.miniwebtool.com/django-secret-key-generator/>, create your secret key, copy it. Open your `projectname/settings/default.py`, find `SECRET_KEY` line, paste your secret key.

#### Other settings stuff
It is good idea to make a **find & replace** within this default settings file as there are some "{{ project_name }}" string left such as `ROOT_URLCONF` or `LOCAL_APPS` variables.

#### Main URL root
You also have to config your application URLs, specific to your own needs. For the beginning, the sample app has only one view that you need to modify its namespace from `projectname/urls.py`, where it *imports HomeView*.

#### local.py (development specific) settings file
Copy `projectname/settings/local.template.py` as `local.py` into the same directory and modify necessary changes. **local.py** is always ignored by **.gitignore**, so this is the machine specific settings mostly for development purposes.

#### Initialize the database
First set the database engine (PostgreSQL, MySQL, etc..) in your settings files; `projectname/settings/default.py` and/or `projectname/settings/local.py`. Of course, remember to install necessary database driver for your engine. Then define your credentials as well. Time to finish it up:

`./manage.py migrate`

### Ready? Go!

`./manage.py runserver`

or

`./manage.py runserver_plus` (Requires Werkzeug)
