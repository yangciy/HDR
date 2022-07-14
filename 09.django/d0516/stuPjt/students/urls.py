from django.urls import path,include
from . import views


app_name='studnets'
urlpatterns = [
    path('register/',views.register,name='register'),
]
