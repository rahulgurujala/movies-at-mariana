from django.urls import path
from .views import movies

urlpatterns = [
    path("movies/", movies, name="movies"),
]
