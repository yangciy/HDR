from django.urls import include, path
from . import views

app_name="board"
urlpatterns = [
    path('list',views.list,name='list'),
]
