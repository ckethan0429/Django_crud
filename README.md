

[TOC]



## 1. models.py 작성(layout)

Model : 부가적인 메타 데이터를 가진 db의 구조(layout) - DB(table)

```python
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
```



## 2. makemigrations : migration 만들기 (설계도)

`$ python manage.py makemigrations` - model 설계도를 만든 것을 기준으로 orm으로 넘어가는 것

`$ python manage.py sqlmigrate boards 0002` - 변환된 sql statement 확인 , 이것이 DB로 들어갈 것



## 3. migrate : DB생성(테이블 생성)

DB로 입력하는 것 : migrate

`$ python manage.py migrate`  

기본적으로 INSTALLED_APPS에 있는 것들도 DB로 migrate해줌.



### * sqlite3 설치 및 환경변수 설정(window) 

| **Precompiled Binaries for Windows** |                                                              |
| :----------------------------------: | ------------------------------------------------------------ |
|                                      | [sqlite-dll-win32-x86-3280000.zip](https://www.sqlite.org/2019/sqlite-dll-win32-x86-3280000.zip) (472.74 KiB) |
|                  ○                   | [sqlite-dll-win64-x64-3280000.zip](https://www.sqlite.org/2019/sqlite-dll-win64-x64-3280000.zip) (786.76 KiB) |
|                  ○                   | [sqlite-tools-win32-x86-3280000.zip](https://www.sqlite.org/2019/sqlite-tools-win32-x86-3280000.zip) (1.70 MiB) |

git bash에 `$ winpty sqlite3` 입력하면 끝 , 종료할 땐 `.exit`

다운로드 파일 위치(나같은 경우 C:\sqlite3에 압축푼 파일들 다 때려넣음) 

환경변수설정 PATH = "C:\sqlite3" 추가

> - 참고 <https://ithub.tistory.com/205> :  shell 설명



$ code ~/.bash_profile에서 alias 

```"alias sqlite3="winpty sqlite3"
alias sqlite3="winpty sqlite3"

export NAVER_CLIENT_ID="클라이언트 ID"

export NAVER_CLIENT_SECRET="씨크릿 키"

```

$ source ~/.bash_profile로 리프레쉬

파이참 종료 후 다시접속



### 해당 DB접속

`$ sqlite3 db.sqlite3`

### DB에 table들 확인

 `.tables`

### 특정 table 확인

 `.schema boards_board` 