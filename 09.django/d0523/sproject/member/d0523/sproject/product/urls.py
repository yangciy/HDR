from django.urls import path,include
from . import views

app_name='product'
urlpatterns = [
    path('pWrite/',views.pWrite,name='pWrite'),
    path('pList/',views.pList,name='pList'),
]
