# Shiny + Django

CMS Shiny is A Django app for adding [R Shiny apps](http://shiny.rstudio.com) to a Django site with django CMS-specific features.

<!-- Detailed documentation is in the "docs" directory. -->

## Quick start

- Edit the project's `settings.py` file.

    - Add `cms_lab_members` and its dependencies to your `INSTALLED_APPS` setting:

        ```python
        INSTALLED_APPS = (
            ...
            'cms_shiny',
        )
        ```

- Include URL configurations for `cms_shiny` in your project's `urls.py` file:

    ```python
    urlpatterns = patterns('',
        ...
        url(r'^shiny_apps/', include('shiny_apps.urls', namespace='shiny_apps')),
        ...
    )
    ```

- Run `python manage.py makemigrations cms_shiny` to create the cms_shiny migrations.

- Run `python manage.py migrate` to create the cms_shiny models.

- Start the development server (`python manage.py runserver`) and visit http://127.0.0.1:8000/

- Create a CMS page and attach the `Shiny App` under `Advanced Settings` for the page.

*Version 0.0.0*
