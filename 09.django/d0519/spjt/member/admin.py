from django.contrib import admin
from member.models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display =['m_no','m_id','m_name']
    
    
admin.site.register(Member,MemberAdmin)

