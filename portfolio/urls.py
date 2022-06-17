from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("", views.HomeView.as_view(), name="home"),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
