from django.urls import path
from .views import MovieListCreateView

urlpatterns = [
    path("movies/", MovieListCreateView.as_view(), name="movie-list-create"),
]
