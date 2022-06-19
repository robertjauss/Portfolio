from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("", views.HomeView.as_view(), name="home"),
        path("about/", views.AboutView.as_view(), name="about"),
        path("resume/", views.ResumeView.as_view(), name="resume"),
        path("projects/", views.ProjectsView.as_view(), name="projects"),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
