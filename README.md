# Shiny + Django

CMS Shiny is A Django app for adding [R Shiny apps](http://shiny.rstudio.com) to a Django site with django CMS-specific features.

<!-- Detailed documentation is in the "docs" directory. -->

## Quick start

- Edit the project's `settings.py` file.

    - Add `cms_shiny` and its dependencies to your `INSTALLED_APPS` setting:

        ```python
        INSTALLED_APPS = (
            ...
            'cms_shiny',
            'easy_thumbnails',
            'filer',
            'mptt',
        )
        ```

    - Specify your media settings, if not already specified:

        ```python
        MEDIA_URL = '/media/'
        MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
        ```

    - Add `filer` and `easy_thumbnail` settings: 

        ```python
        # For filer's Django 1.7 compatibility
        MIGRATION_MODULES = {
            ...
            'filer': 'filer.migrations_django',
        }

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
        ```

- Include URL configurations for `cms_shiny` in your project's `urls.py` file:

    ```python
    urlpatterns = patterns('',
        ...
        url(r'^shiny_apps/', include('cms_shiny.urls', namespace='cms_shiny')),
        ...
    )
    ```

- Run `python manage.py makemigrations cms_shiny` to create the cms_shiny migrations.

- Run `python manage.py migrate` to create the cms_shiny models.

- Start the development server (`python manage.py runserver`) and visit http://127.0.0.1:8000/

- Create a CMS page and attach the `Shiny Apps App` under `Advanced Settings` for the page.

*Version 0.1.0*
