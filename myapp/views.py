from django.shortcuts import render, HttpResponse
from .models import TodoItem
# Create your views here.


def home(request):
    # name of template
    # needs to be inside the `templates` folder
    return render(request, "home.html")

def todos(request):
    # getting all items from database
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})
