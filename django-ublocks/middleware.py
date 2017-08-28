from django.apps import apps
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import render

from .models import Route


class uBlockRouteMiddleware(object):

    def __init__(self, get_response=None):
        if not apps.is_installed('django.contrib.sites'):
            raise ImproperlyConfigured(
                "You cannot use uBlockRouteMiddleware when "
                "django.contrib.sites is not installed."
            )

    def process_response(self, request, response):
        # No need to check for a redirect for non-404 responses.
        if response.status_code != 404:
            return response

        full_path = request.get_full_path()
        current_site = get_current_site(request)

        r = None

        try:
            r = Route.objects.get(site=current_site, path=full_path)
        except Route.DoesNotExist:
            pass

        if settings.APPEND_SLASH and not request.path.endswith('/'):
            # Try appending a trailing slash.
            path_len = len(request.path)
            full_path = full_path[:path_len] + '/' + full_path[path_len:]

            try:
                r = Route.objects.get(site=current_site,path=full_path)
            except Route.DoesNotExist:
                pass

        if r is not None:
            return render(request,'ublocks/base.html',dict(route=r))

        # No redirect was found. Return the response.
        return response