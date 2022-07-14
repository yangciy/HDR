from django.urls import path,include
from . import views

app_name='freeboard'
urlpatterns = [
    # fList.html연결
    path('fList/',views.fList,name='fList'),
    path('<str:f_no>/fView/',views.fView,name='fView'),
    path('fWrite/',views.fWrite,name='fWrite'),
    path('<str:f_no>/fDelete/',views.fDelete, name='fDelete'),
    path('<str:f_no>/fUpdate/',views.fUpdate, name='fUpdate'),
]