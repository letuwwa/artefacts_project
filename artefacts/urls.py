from django.urls import path

from .views import ArtefactsListView


urlpatterns = [
    path("artefact/", ArtefactsListView.as_view()),
]
