from django.urls import path, include
from . import views

app_name='fboard'
urlpatterns = [
    path('<int:nowpage>/fList/',views.fList,name='fList'),
    path('<int:nowpage>/fWrite/',views.fWrite,name='fWrite'),
    path('<str:fNum>/<int:nowpage>/fView/',views.fView,name='fView'),
    path('<str:fNum>/<int:nowpage>/fReply/',views.fReply,name='fReply'),
    path('<str:fNum>/<int:nowpage>/fDelete/',views.fDelete,name='fDel'),
    path('<str:fNum>/<int:nowpage>/fUpdate/',views.fUpdate,name='fUpdate'),
]
