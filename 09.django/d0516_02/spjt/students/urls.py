from . import views
from django.urls import path,include

app_name='studnets'
urlpatterns = [
    path('register/',views.register,name='register'),
]