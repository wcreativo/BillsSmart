from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from apps.users.views import LoginView, RegisterUserView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", RegisterUserView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from drf_spectacular.views import (SpectacularAPIView,
                                       SpectacularRedocView,
                                       SpectacularSwaggerView)

    urlpatterns += [
        path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
        path(
            "api/docs/",
            SpectacularSwaggerView.as_view(url_name="schema"),
            name="api-docs",
        ),
        path(
            "api/schema/redoc/",
            SpectacularRedocView.as_view(url_name="schema"),
            name="redoc",
        ),
    ]

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
