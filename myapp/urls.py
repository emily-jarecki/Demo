from django.urls import path
from . import views

urlpatterns = [
    # in the `views` file with the `home` function
    path("", views.home, name="home"),
    path("todos/", views.todos, name="Todos")
]