# Go Weby CMS

## Custom CMS build with Django Web and ReST Frameworks

About
------

Go Weby is an open-source platform built on the Django Web Framework.
It intents to be an ecosystem of reusable Django apps, for the Web.

This project is in development progress. The basic idea is the construction of an easy to use
CMS for multiple purpose web applications  .


Installation for Development
----------------------------
### Install and setup using Docker
TODO: Fill the instruction for the docker setup

#### Install the docker toolbox
     The first step is to install the [url]Docker Toolbox.

#### Run manage.py using
     docker-compose run web python manage.py migrate


### Install and setup Virtualenv

- $ sudo pip install virtualenv
- $ virtualenv -p /usr/bin/python3 envname
- $ source envname/bin/activate

### Install project dev dependencies

#### Install Front End dependencies

First install bower and Gulp task runner

  - $ npm install -g gulp bower

Install npm and bower dependencies

  - $ npm install

  - $ bower install

#### Python & Django dependencies

  Virtual environment use is strongly recommended

    - $ pip install -r requirements/dev.txt

  Time for database setup

  - make start # This will make the first migrations, and a root superuser creation


### Build Assets

Use the Gulp Task Runner

Tasks:

- $ gulp sass # compiles sass to css and uses an autoprefixer for the css
- $ gulp sass:watch # watches predefined sources for changes and runs `gulp sass`
- $ gulp # Compilation of sass and watch


Features
---------

Current features include:

  TODO: Add current features info


Future features include:

  TODO: Add future features info
