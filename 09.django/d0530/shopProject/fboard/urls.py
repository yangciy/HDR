from django.urls import path, include
from . import views

app_name='fboard'

urlpatterns = [
    path('<int:nowpage>/<str:category>/<str:searchword>/fList',views.fList,name='fList'),
    path('<int:nowpage>/<str:category>/<str:searchword>/fWrite',views.fWrite,name='fWrite'),
    path('<str:f_no>/<int:nowpage>/<str:category>/<str:searchword>/fView',views.fView,name='fView'),
    path('<str:f_no>/<int:nowpage>/<str:category>/<str:searchword>/fDelete',views.fDelete,name='fDelete'),
    path('<str:f_no>/<int:nowpage>/<str:category>/<str:searchword>/fUpdate',views.fUpdate,name='fUpdate'),
    path('<str:f_no>/<int:nowpage>/<str:category>/<str:searchword>/fReply',views.fReply,name='fReply'),
    path('public_list',views.public_list,name='public_list'),
    path('event/',views.event,name='event'),
    # 이벤트 view
    path('event_view/',views.event_view,name='event_view'),
    # 댓글 list
    path('commList/',views.commList,name='commList'),
    path('commWrite/',views.commWrite,name='commWrite'),
    path('commDelete/',views.commDelete,name='commDelete'),
    # 댓글수정저장 updateOk
    path('commUpdateOk/',views.commUpdateOk,name='commUpdateOk'),
]
