from django.urls import include, path
from . import views
app_name='students'         # 페이지 이동 할 때
urlpatterns = [
    path("stuWrite/",views.stuWrite,name='stuWrite'),               # 학생등록
    path("stuWriteOk/",views.stuWriteOk,name='stuWriteOk'),         # 학생저장
    path("stuList/",views.stuList, name='stuList'),                 # 학생전체리스트
    path("<str:s_no>/stuView/",views.stuView,name='stuView'),       # 학생상세리스트
    path("<str:s_no>/stuUpdate/",views.stuUpdate, name='stuUpdate'),# 학생정보수정
    path("stuUpdateOk/",views.stuUpdateOk, name='stuUpdateOk'),     # 수정한 내용 저장
    path("<str:s_no>/stuDelete/",views.stuDelete, name='stuDelete'),           # 학생정보삭제
    ]
