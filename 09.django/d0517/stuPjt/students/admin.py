from django.contrib import admin
from students.models import Student


# admin.site.register(Student)
# @사용 - decorator 잠식자
# @admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['s_name','s_major','s_age']
    
admin.site.register(Student,StudentAdmin)