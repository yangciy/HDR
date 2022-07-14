from django.urls import path, include
from . import views

app_name='fboard'
urlpatterns = [
    path('<int:nowpage>/fList/',views.fList,name='fList'),
    path('<int:nowpage>/fWrite/',views.fWrite,name='fWrite'),
    path('<str:f_no>/<int:nowpage>/fView/',views.fView,name='fView'),
    # 답글달기
    path('<str:f_no>/<int:nowpage>/fReply/',views.fReply,name='fReply'),
    path('<str:f_no>/<int:nowpage>/fDelete',views.fDelete,name='fDelete'),
    path('<str:f_no>/<int:nowpage>/fUpdate',views.fUpdate,name='fUpdate'),
]