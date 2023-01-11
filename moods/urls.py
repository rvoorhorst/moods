from django.contrib import admin
from django.urls import path

from moods.views import HomeFormView, PlaylistTemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeFormView.as_view(), name="home"),
    path("playlist/", PlaylistTemplateView.as_view(), name="playlist"),
]
