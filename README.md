# django-sample-app

django-sample-app is a **minimal** sample application to start developing your web project immediately on [Django framework](https://www.djangoproject.com/). 

The sample application comes with:

* [Modernizr](http://modernizr.com/) v2.6.2
* [jQuery](http://jquery.com/) v1.9.1
* [jQuery UI](http://jqueryui.com/) v1.9.2
* [Twitter Bootstrap](http://twitter.github.com/bootstrap/) v2.3.0
* [Font Awesome](http://fortawesome.github.com/Font-Awesome/) v3.0

that are glued together with [initializr](http://www.initializr.com/). And its current `requirements.txt` file is:

```
Django==1.5.1
South==0.7.6
django-admin-tools==0.5.1
django-debug-toolbar==0.9.4
django-extensions==1.1.1
ipython==0.13.2
psycopg2==2.5
readline==6.2.4.1
six==1.3.0
wsgiref==0.1.2
```

## Installation

### 1. virtualenv / virtualenvwrapper
You should already know what is [virtualenv](http://www.virtualenv.org/), preferably [virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/) at this stage. So, simply create it for your own project, where `myproject` is the name of your project:

`$ mkvirtualenv --clear myproject`

### 2. Download
Now, you need the *django-sample-app* project files in your workspace:

    $ cd /path/to/your/workspace
    $ git clone git://github.com/kirpit/django-sample-app.git myproject && cd myproject
    $ mv sampleapp myproject

### 3. Requirements
Right there, you will find the *requirements.txt* file that has all the great debugging tools, django helpers and some other cool stuff. To install them, simply type:

`$ pip install -r requirements.txt`

Remember to install *readline* with "easy_install" that is necessary for IPython to work properly:

`$ easy_install -a readline`

### 4. Static files for django-admin
You need to create a symbolic link to your django admin static folder under your "static_extra" directory. I assume you are still in the same, project's root directory:

`$ ln -s /path/to/site-packages/django/contrib/admin/static/admin static_extra/admin`

You can find out the location of your "site-packages" folder by the following command if necessary:

`$ python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())"`

### 5. Tweaks

#### wsgihandler.py
`wsgihandler.py` file is necessary for WSGI gateways (such as uWSGI) to run your Django application and also required from Django itself. You definitely want to change `sampleapp.settings` value in this file to whatever you name your application (e.g. `myproject.settings`).

#### SECRET_KEY
Go to <http://www.miniwebtool.com/django-secret-key-generator/>, create your secret key, copy it. Open your `myproject/settings/default.py`, find `SECRET_KEY` line, paste your secret key.

#### Other settings stuff
It is good idea to make a **find & replace** within this default settings file as there are some "sampleapp" string left such as `ROOT_URLCONF` or `LOCAL_APPS` variables, but not only.

#### Main URL root
You also have to config your application URLs, specific to your own needs. For the beginning, the sample app has only one view that you need to modify its namespace from `myproject/urls.py`, where it *imports HomeView*.

#### local.py (development specific) settings file
Copy `myproject/settings/local.template.py` as `local.py` into the same directory and modify necessary changes. **local.py** is always ignored by **.gitignore**, so this is the machine specific settings usually for development purposes. 

#### Initialize the database
You should have already created your database and set the credentials in your `local.py` now. Time to finish it up:

`./manage.py syncdb` and `./manage.py migrate`

### Ready? Go!

`./manage.py runserver`

or

`./manage.py runserver_plus`
