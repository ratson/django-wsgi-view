django-wsgi-view
================

.. image:: https://img.shields.io/pypi/v/django-wsgi-view.svg
    :target: https://pypi.python.org/pypi/django-wsgi-view
    :alt: Latest PyPI version
    :crossorigin: anonymous

Embed WSGI application as Django view.

Requirements
------------

- Python >= 3.6
- Django >= 1.10

Installation
------------

You can install ``django-wsgi-view`` via `pip`_ from `PyPI`_::

    $ pip install django-wsgi-view

.. _`pip`: https://pypi.python.org/pypi/pip/
.. _`PyPI`: https://pypi.python.org/pypi

Usage
-----

``urls.py`` module in your project:

.. code:: python

    from django.conf.urls import url
    from wsgi_view import WsgiView

    urlpatterns = [
        url(r'^sub-app(/.*)', WsgiView.as_view(application='wsgi.app')),
    ]
