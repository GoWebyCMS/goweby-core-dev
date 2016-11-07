==========
# Hatchery
## A Django Boiler Plate for Web
==========

Hatchery
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

### Build Assets

Using the gulp task runner

Tasks:

- `gulp sass`: compiles sass to css and uses an autoprefixer for the css
- `gulp sass:watch`: watches predefined sources for changes and runs `gulp sass`
- `gulp`: runs the 2 above



Features
---------

Current features include:

* support for multiple channels (e.g. technical vs business)
* use of Creole (optional) and Markdown as markup format
* Atom and RSS feeds
* public but secret urls for unpublished blog posts for easier review
