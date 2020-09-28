"""
Main URL mapping configuration file.

Include other URLConfs from external apps using method `include()`.

It is also a good practice to keep a single URL to the root index page.

This examples uses Django's default media
files serving technique in development.
"""

from django.conf import settings
from django.contrib import admin
from django.contrib.admindocs import urls as admindocs_urls
from django.urls import include, path
from django.views.generic import TemplateView
from health_check import urls as health_urls
from rest_framework import routers

from server.apps.images.viewsets import ImagesViewSet

admin.autodiscover()

router = routers.DefaultRouter()
router.register("images", ImagesViewSet)

urlpatterns = [
    # Apps:
    # # DRF:
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    # Health checks:
    path("health/", include(health_urls)),  # noqa: DJ05
    # django-admin:
    path("admin/doc/", include(admindocs_urls)),  # noqa: DJ05
    path("admin/", admin.site.urls),
    # Text and xml static files:
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="txt/robots.txt",
            content_type="text/plain",
        ),
    ),
    path(
        "humans.txt",
        TemplateView.as_view(
            template_name="txt/humans.txt",
            content_type="text/plain",
        ),
    ),
]

if settings.DEBUG:  # pragma: no cover
    import debug_toolbar  # noqa: WPS433
    from django.conf.urls.static import static  # noqa: WPS433

    urlpatterns = (
        [
            # URLs specific only to django-debug-toolbar:
            path("__debug__/", include(debug_toolbar.urls)),  # noqa: DJ05
        ]
        + urlpatterns
        + static(
            # Serving media files in development only:
            settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT,
        )
    )
