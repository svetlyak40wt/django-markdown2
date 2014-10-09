django-markdown2
----------------

[![changelog](http://allmychanges.com/p/python/django-markdown2/badge/)](http://allmychanges.com/p/python/django-markdown2/?utm_source=badge)

This is a simple app, which supplies a single template tag for
markdown markup.

Dependencies
============

django-markdown2 depends on python-markdown2, which can be found
at http://code.google.com/p/python-markdown2.

Installation and usage
======================

* Place `django_markdown2` somewhere in your `PYTHONPATH`.
* Add `django_markdown2` to you `INSTALLED_APPS`.
* In any template do:

        {% load md2 %}
        {{ variable|markdown }}

* Or specify additional extensions:

        {% load md2 %}
        {{ variable|markdown:"safe, code-friendly, code-color" }}

* Also, if you use my recent markdown2-with-blackjack from http://pypi.aartemenko.com,
  then you can pass additional options to code-color extension:

        {% load md2 %}
        {{ variable|markdown:"safe, code-friendly, code-color: noclasses|linenos" }}

  Options from this example switch off css classes and turn on line numbers.


Contribution
============

Code for this application available at:
<http://github.com/svetlyak40wt/django-markdown2>

