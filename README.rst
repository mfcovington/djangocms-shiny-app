*******************
djangocms-shiny-app
*******************

``djangocms-shiny-app`` is a Django app for adding `R Shiny apps <http://shiny.rstudio.com>`_ to a Django site with django CMS-specific features.

Source code is available on GitHub at `mfcovington/djangocms-shiny-app <https://github.com/mfcovington/djangocms-shiny-app>`_.


.. contents:: :local:


Installation
============

**PyPI**

.. code-block:: sh

    pip install djangocms-shiny-app


**GitHub (development branch)**

.. code-block:: sh

    pip install git+http://github.com/mfcovington/djangocms-shiny-app.git@develop


Configuration
=============


- `Install django CMS and start a project <http://docs.django-cms.org/en/latest/introduction/install.html>`_, if one doesn't already exist.


- Unless you use this app as part of `djangocms-lab-site <https://github.com/mfcovington/djangocms-lab-site>`_ or plan to style the app from scratch, you will want to choose the ``Use Twitter Bootstrap Theme`` option (when running ``djangocms``) and then edit the resulting ``templates/base.html``.

  - This will add style that looks like Bootstrap 2. To use Bootstrap 3 styling, remove the following line for the ``bootstrap-theme.min.css`` stylesheet from ``templates/base.html``:

    .. code-block:: python

        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.x.x/css/bootstrap-theme.min.css">

  - The default menu settings for django CMS using Bootstrap will allow the user to access specific lab members via a dropdown menu, but will not give easy access to the summary page of all Shiny apps. To fix this do one of the following:

    - In ``templates/base.html``, change ``{% show_menu 0 1 100 100 "menu.html" %}`` to ``{% show_menu 0 0 100 100 "menu.html" %}``, or

    - Use a split button dropdowns by changing that line to `{% show_menu 0 100 1 1 '_menu.html' %}` and populate `_menu.html` as done in `djangocms-lab-site <https://github.com/mfcovington/djangocms-lab-site>`_.


- Edit the project's ``settings.py`` file.

  - Add ``cms_shiny`` and its dependencies to ``INSTALLED_APPS``:

  .. code-block:: python

      INSTALLED_APPS = (
          # ...
          'cms_shiny',
          'easy_thumbnails',
          'filer',
          'mptt',
      )


  - Add ``easy_thumbnail`` settings: 

  .. code-block:: python

      # For easy_thumbnails to support retina displays (recent MacBooks, iOS)
      THUMBNAIL_HIGH_RESOLUTION = True
      THUMBNAIL_QUALITY = 95
      THUMBNAIL_PROCESSORS = (
          'easy_thumbnails.processors.colorspace',
          'easy_thumbnails.processors.autocrop',
          'filer.thumbnail_processors.scale_and_crop_with_subject_location',
          'easy_thumbnails.processors.filters',
      )
      THUMBNAIL_PRESERVE_EXTENSIONS = ('png', 'gif')
      THUMBNAIL_SUBDIR = 'versions'


- To access ``cms_shiny`` pages without using a django CMS AppHook, include URL configurations for ``cms_shiny`` in your project's ``urls.py`` file:

  - For **Django 1.7**:

    .. code-block:: python

        urlpatterns = patterns('',
            # ...
            url(r'^shiny_apps/', include('cms_shiny.urls', namespace='cms_shiny')),
            # ...
        )


  - For **Django 1.8**:

    .. code-block:: python

        urlpatterns = [
            # ...
            url(r'^shiny_apps/', include('cms_shiny.urls', namespace='cms_shiny')),
            # ...
        ]


Migrations
==========

Create and perform ``cms_shiny`` migrations:

.. code-block:: sh

    python manage.py makemigrations cms_shiny
    python manage.py migrate


Usage
=====

- Start the development server:

.. code-block:: sh

    python manage.py runserver


- Visit: ``http://127.0.0.1:8000/``
- Create a CMS page and then:

  - Attach the ``Shiny Apps App`` under ``Advanced Settings`` for the page, **OR**
  - Insert the ``Shiny App Plugin`` into a placeholder field.


*Version 0.1.3*
