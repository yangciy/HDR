from django.contrib import admin
from board.models import Board

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ['Z_no','Z_title','Z_createdate']
    
    