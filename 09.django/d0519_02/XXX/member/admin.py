from django.contrib import admin
from member.models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display =['s_no','s_id','s_name']
    
    
admin.site.register(Member,MemberAdmin)