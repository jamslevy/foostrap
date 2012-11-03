========
foostrap
========

Flask + Heroku + Bootstrap = foostrap

``foostrap`` is a skeleton project helps you get a Twitter Bootstrap based
Flask app running on Heroku as fast as possible.

Some of the things ``foostrap`` provides are:

Flask
-----


* Sensible project layout
* Setuptools support (MANIFEST.in entries for static and template files, setup.py)
* Basic pip requirements file
* Useful Flask extensions (SSLify, DebugToolbar)


Heroku
------

* Foreman support out of the box, ``.env`` sample and default ``Procfile``
* Better environment variable handling via ``envparse``


Bootstrap
---------

* Bootstrap default layout.html
* Script to fetch Bootstrap and JQuery assets


Git
---

* Sensible ``.gitignore``
* Pre-commit hook to run ``pep8`` and ``nosetests`` before commiting


Installation
============

::

    ./tools/setup-app YOUR-APP-NAME

    
Create a virualenv for your app::

    mkvirtualenv YOUR-APP-NAME --no-site-packages
    workon YOUR-APP-NAME


Copy ``.env`` sample and edit it to your liking::

    cp etc/env.sample .env


Run it::

  foreman start
