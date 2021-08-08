from django.urls import path

from .views import ActualUrlView, ShortenerView

urlpatterns = [
    path("short-url/", ShortenerView.as_view()),
    path("<str:short_url>", ActualUrlView.as_view())
]
