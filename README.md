# Hatchery
## A custom Django CMS

About
------

Hatchery is an open-source platform built on the Django Web Framework.
It intents to be an ecosystem of reusable Django apps, for the Web.

This project is in development progress. The basic idea is the construction of an easy to use
CMS for multiple purpose web applications  .


Installation for Development
---------------
### Install and setup Virtualenv

- $ sudo pip install virtualenv
- $ virtualenv -p /usr/bin/python3 envname
- $ source envname/bin/activate

### Install project dev dependancies

* First activate the environment
- $ pip install -r requirements/dev.txt


### Build Assets

Using the gulp task runner

Tasks:

- `gulp sass`: compiles sass to css and uses an autoprefixer for the css
- `gulp sass:watch`: watches predefined sources for changes and runs `gulp sass`
- `gulp`: runs the 2 above


Features
---------

Current features include:

  TODO: Add current features info


Future features include:

  TODO: Add future features info
