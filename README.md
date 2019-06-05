

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



`$ python manage.py shell` - django DB를 작성할 수 있는 shell

-> 매일 치기 싫으면 `pip install django-extensions`

INSTALLED_APPS =[ ] - 에 추가해야함.

`$ python manage.y shell_plus`를 하면 django에 대한 모든것 import 됨.



> ### 1.
>
> from boards.models import Board
> Board.objects.all()  (select * from boards_board와 같은 의미)
> -><QuerySet []>
>
> board = Board()
> board.title = 'first'
> board.content = 'django!!'
> -><Board: Board object (None)>
> board.save()
> board
> -><Board: Board object (1)>
>
> ### 2.
>
> board=Board(title='second',content='django!!!')
> board.save()
>
> ### 3.
>
> Board.objects.create(title='third',content='django!!!!')
> save가 따로 필요없음.



 

### * 유효성 검증

board.full_clean()



## 데이터 조회(C)

`Board.objects.all()` 

조회할 때 표현 바꾸기 

`models.py`에서 해당 메소드 추가

```python
def __str__(self):
    return f'{self.id}글 - {self.title}: {self.content}'
```

board = Board.objects.filter(id=1)  -여러개

<QuerySet [<Board: 1글 - first: django!!>]>



SELECT * FROM boards WHERE id=1

board = Board.objects.get(pk=1)

board = Board.objects.get(id=1)

board로 확인

boards = Board.objects.filter(title__contains='fi')

boards = Board.objects.filter(content__endwith='!')

boards = Board.objects.order_by('title') - 오름차순

boards = Board.objects.order_by('-title') - 내림차순

boards[1] , boards[1:3]



## 데이터 수정 (R)board = Board.objects.get(pk=1)

 board.title = 'byebye'

 board.save()

board 

### * save() - board 객체에 id가 없으면 추가, 있으면 수정

### create 

1. 글을 작성하는 페이지를 render 할 view 함수
2. db에 값을 저장해주는 view 함수 필요(orm db에 값을 저장)





dir(board) : board란 객체로 쓸수있는 메소드





## get과 post 차이

- html 파일 줘(GET)

- ~한 레코드(글)을 생성해줘!(POST)

- 데이터 관련정보는 url에 노출되면 안된다.

- DB를 건드리기 떄문에 최소한의 신원확인이 필요하다 . 즉, csrf token을 통해 검증된 요청을 받아야한다.

- [결론] : POST요청은 html문서를 렌더링하는 것이 아니다. 요청을 처리하고나서 결과를 보여주는게 아니라, 결과를 보여위한 페이지로 넘겨줘야한다.(**redirect**)

- ```python
  from django.shortcuts import render, redirect
  ```



## 테이블 생성한 이후에 admin 생성

`$ python manage.py createsuperuser`

`$ sqlite3 db.sqlite3`

`sqlite> .tables`

`sqlite> select * from auth_user;`

