*******************
djangocms-shiny-app
*******************

``djangocms-shiny-app`` is a Django app for adding `R Shiny apps <http://shiny.rstudio.com>`_ to a Django site with django CMS-specific features.

.. contents:: :local:


Installation
============

**PyPI**

.. code-block:: sh

    pip install djangocms-shiny-app

**GitHub**

.. code-block:: sh

    pip install https://github.com/mfcovington/djangocms-shiny-app/releases/download/0.1.2/djangocms-shiny-app-0.1.2.tar.gz


Configuration
=============

Do the following in ``settings.py``:

- Add ``cms_shiny`` and its dependencies to ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'cms_shiny',
        'easy_thumbnails',
        'filer',
        'mptt',
    )


- Specify your media settings, if necessary:

.. code-block:: python

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


- Add ``filer`` and ``easy_thumbnail`` settings: 

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


To access ``cms_shiny`` pages without using a django CMS AppHook, include URL configurations for ``cms_shiny`` in your project's ``urls.py`` file:

.. code-block:: python

    urlpatterns = patterns('',
        ...
        url(r'^shiny_apps/', include('cms_shiny.urls', namespace='cms_shiny')),
        ...
    )


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


*Version 0.1.2*
