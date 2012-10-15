# django-sample-app

django-sample-app is a **minimal** sample application to start developing your web project immediately on [Django framework](https://www.djangoproject.com/). 

The sample application comes with:

* [H5BP](http://html5boilerplate.com/) 4.0.0
* [jQuery](http://jquery.com/) 1.8.2
* [Modernizr](http://modernizr.com/) 2.6.1
* [Twitter Bootstrap](http://twitter.github.com/bootstrap/) 2.1.1

that are combined together with [initializr](http://www.initializr.com/). And its current `requirements.txt` file is:

```
Django==1.4.1
South==0.7.6
django-admin-tools==0.4.1
django-debug-toolbar==0.9.4
django-extensions==0.9
django-pdb==0.3.2
ipython==0.13
psycopg2==2.4.5
readline==6.2.2
wsgiref==0.1.2
```

## Installation

### 1. virtualenv / virtualenvwrapper
You should already know what is [virtualenv](http://www.virtualenv.org/), preferably [virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/) at this stage. So, simply create it for your own project, where `myproject` is the name of your project:

`$ mkvirtualenv --clear myproject`

### 2. Download
Now, you need the *django-sample-app* project files in your workspace:

`$ cd /path/to/your/workspace`  
`$ git clone git://github.com/kirpit/django-sample-app.git`  
`$ mv django-sample-app myproject && cd myproject`  
`$ mv sampleapp myproject`  

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

### 5. Settings

#### SECRET_KEY
Go to <http://www.miniwebtool.com/django-secret-key-generator/>, create your secret key, copy it. Open your `myproject/settings/default.py`, find `SECRET_KEY` line, paste your secret key.

#### Other settings stuff
It is good idea to make a **find & replace** within this default settings file as there are some "sampleapp" string left such as `ROOT_URLCONF` or `LOCAL_APPS` variables, but not only.

#### local.py (development specific) settings file
Copy `myproject/settings/local.template.py` as `local.py` into the same directory and modify necessary changes. **local.py** is always ignored by **.gitignore**, so this is the machine specific settings usually for development purposes. 

#### Initialize the database
You should have already created your database and set the credentials in your `local.py` now. Time to finish it up:

`./manage.py syncdb` and `./manage.py migrate`

Ready? Go!

`./manage.py runserver_plus`