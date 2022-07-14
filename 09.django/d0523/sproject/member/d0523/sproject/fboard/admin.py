from django.contrib import admin
from fboard.models import Fboard

@admin.register(Fboard)

class FboardAdmin(admin.ModelAdmin):
    list_display=['fNo','fmember','fTitle','fUpdatedate']