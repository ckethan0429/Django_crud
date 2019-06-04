from django.db import models

# Create your models here.
class Board(models.Model):
    # id (pk) 는 기본적으로 처음 테이블 생성시 자동생성된다.
    # id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=10) #string의 길이의 제한
    content = models.TextField()
    # auto_now_add : 생성일자 / db가 최초 저장시에만 적용
    # auto_now : 수정일자 / db가 새로 저장될떄마다 갱신
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


