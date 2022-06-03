from django.urls import path

from .views import ArtefactsListView


urlpatterns = [
    path("", ArtefactsListView.as_view()),
]
