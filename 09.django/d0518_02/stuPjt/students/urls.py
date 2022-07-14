from django.urls import include, path
from . import views

app_name='students'
urlpatterns = [
    path("stuWrite/",views.stuWrite,name='stuWrite'),
    path("stuWrtieOk/",views.stuWriteOk,name="stuWriteOk"),
    path('stuList/',views.stuList,name='stuList'),
    path("<str:s_no>/stuView",views.stuView,name='stuView'),
    path("<str:s_no>/stuUpdate/",views.stuUpdate, name='stuUpdate'),
    path("stuUpdateOk/",views.stuUpdateOk, name='stuUpdateOk'),     
    path("<str:s_no>/stuDelete/",views.stuDelete, name='stuDelete'),        
    
]
