# Django Views: Functions, Classes, and Generics

This repository contains the code used in my DjangoCon 2015
presentation. All other materials may be accessed
[here](http://andrewsforge.com/presentation/django-views-functions-classes-generics/).

**NB**: To ease setup of this demonstration, the Django Secret Key has
not been removed from the settings.py file. This site should therefore
**never** be used for production purposes.

## Purpose

The main purpose of this repository is to showcase the code changes in
[`src/viewsapp/views.py`](https://github.com/jambonrose/djangocon2015-views/blob/master/src/viewsapp/views.py).
There are several relevant states (stored in the repo as git tags; click the
links to see each one; in order of appearance in the presentation): 

- [`function-views`](https://github.com/jambonrose/djangocon2015-views/blob/function-views/src/viewsapp/views.py) 
    - demonstration of function views with `require_http_methods` and related
      shortcuts
- [`class-based-views`](https://github.com/jambonrose/djangocon2015-views/blob/class-based-views/src/viewsapp/views.py)
    - demonstration of class-based views
- [`generic-views`](https://github.com/jambonrose/djangocon2015-views/blob/generic-views/src/viewsapp/views.py)
    - demonstration of generic class-based views
- [`django-decorator-plus`](https://github.com/jambonrose/djangocon2015-views/blob/django-decorator-plus/src/viewsapp/views.py)
    - function views with the expanded `require_http_methods` from my
      [`django-decorator-plus`](https://pypi.python.org/pypi/django-decorator-plus)
      project

## Setup

The project is built in Python 3.4 and Django 1.8. To download the
repository, please use:

    $ git clone https://github.com/jambonrose/djangocon2015-views.git
    $ cd djangocon2015-views

Using a virtual environment (such as
[`virtualenvwrapper`](https://pypi.python.org/pypi/virtualenvwrapper))
is highly recommended.

    $ mkvirtualenv djangocon2015-views
    $ pip install -r requirements.txt

This will allow you to run the Jupyter Notebook, as demonstrated below.

    $ jupyter notebook Callable_Primer.ipynb

The Django project code is stored in the `src/` directory. It uses the
default Django configuration (the SQLite database), allowing you to run
the project immediately:

    $ cd src
    $ ./manage.py migrate
    $ ./manage.py runserver

Only two webpages are defined:

- http://127.0.0.1:8000/create/
- http://127.0.0.1:8000/django/

## Helpful Links

- [Classy Class-Based Views](http://ccbv.co.uk/)
- [django-decorator-plus](https://pypi.python.org/pypi/django-decorator-plus)
