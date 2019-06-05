from django.contrib import admin
from .models import Board
# Register your models here.
class BoardAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'created_at', 'updated_at', ]

admin.site.register(Board, BoardAdmin) # 컬럼생성후 클래스를 등록해줘야함
