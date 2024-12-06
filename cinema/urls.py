from django.urls import path

from cinema.views import *

app_name = "cinema"
urlpatterns = [
    path("cinema/movies/", list_create_movie, name="list_create_movie"),
    path(
        "cinema/movies/<int:pk>/",
        show_update_delete_movie,
        name="show_update_delete_movie",
    ),
]
