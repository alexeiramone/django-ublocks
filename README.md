# Django uBlocks
Standarized HTML blocks paired with a common model instance. Easy way to create prototypes and page sections with database-persistent context.

## PROOF-OF-CONCEPT, DO NOT USE IN PRODUCTION

## DEMO Django 1.7

1. Just CD `demo17` and run `python manage.py runserver`
2. Admin username: test, pass test1234

## Install

1. Add `'django-ublocks.apps.uBlocksConfig',` in your `INSTALLED_APPS` settings;
2. Add `url(r'^ublocks/', include('ublocks.urls')),` in your `urls.py` 

## TODO

- Resolve Dash issue in the folder (can't import properly)
- Template Importer/parser (choices feeder)
- Fix templates
- Better GET Queries in views and templatetags
- Better TinyMCE Configuration
- Decision: forms versus TinyMCE (hidden and unstyled elements)
- Remove old project's garbage
- Routes and Middleware
- Use better classifiers in `setup.py`
