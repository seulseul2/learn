ORM은 python과 sql을 연결해주는 해석기같은 느낌인듯

[X] -> 확인되었다는 뜻.



0002_auto_ -> 두번째 설계도가 만들어졌다.

dependenceis : 첫번째 설계도에 의존을 하고 있다.

----------

반드시 기억해야 할 migration 3단계

1. models.py : model 변경사항 발생 시
2. $ python manage.py makemigrations : migrations 파일 생성
3. $ python manage.py migrate : DB반영

-------------

DB Api

---------------------

CREATE

만드는 3가지 방법이 있음.

근데 보통 2번째 방법을 사용했다

article = Article(title=title, content=content)

...

... -> 여기 사이 과정에 유효성 검사를 하기 위해서!

...

article.save()



READ

all() : 전체 queryset 반환

get() : 한개만 찾을때 쓰는 거. 없으면 없다고 말해주고, 두개 이상 찾으려하면 예외발생시킴. 그래서 PK를 써줘야함(고유성)

filter() : get이랑은 다르게, 없으면 빈 쿼리셋 가져다주고 두 개 이상이어도 찾아주는 녀석



UPDATE

조회를 먼저 하고 -> 수정 한 다음에 -> save() 잊지 않기



DELETE

딕셔너리를 반환함

---------

__ModelForm을 왜 써야하는가?__

Form이 하는 역할 : 사용자의 정보 입력을 받는 역할. 이를 서버에 저장.

Form - DB가 굉장히 밀접한 관련이 있다. 그래서 DB에 저장된 구조를 그대로 Form에 쓸 수 있다면 정말 편하게 쓸 수 있을 것이다. 그럴때는 ModelForm

반면, DB와 관련은 없지만 사용자 정보를 받아야 할 때는 Form을 더 편리하게 사용할 수 있을 것.

그래서 웹을 보면 대충 데이터 구조를 유추할 수 있을 것이다. ssafy 사이트를 예로 들면, 앞에 *가 붙어있는 것은 필수 사항이므로 NOT NULL, 반면 첨부파일은 선택사항이니 그런 옵션이 없을 것이다.

-------

__모델폼이 쉽게 해주는 것__

1. 모델 필드 속성에 맞는 html element를 만들어 줌
2. 이를 통해 받은 데이터를 view 함수에서 유효성 검사를 할 수 있도록 함