p.8 ~

GET(조회) POST(작성) PUT(수정) DELETE(삭제)



p10 ~

URI에 대해 알아보겠습니다.

URL과 URN



p.17 ~

__Query__

Query String Parameter / 식별자

GET방식 썼을때 추가적으로 전송되었던 매개 변수



__Fragment__

브라우저 내 특정 부분을 보여주는 방법. 예를 들어 부트스트랩 # 주소복사를 하면 해당 주소 + 해당 위치를 정확하게 렌더링 해준다.



__REST__

설계 방법론은 규약이나 약속이 아니라, 방법론 중에 하나다. REST 원리를 따르는 시스템 == RESTful

자원을 어떻게 배치시킬 것이냐에 대한 고민이다.

__핵심 규칙은 2가지__ -> 지키는 편이 훨씬 좋다!

- '정보'는 URI로 표현
- 자원에 대한 '행위'는 HTTP Method로 표현 (GET, POST, PUT, DELETE) - RCUD 순



__JSON__

JavaScript의 표기법을 따른 __단순 문자열.__ 한 문자열인데 python으로 딕셔너리로 파싱(해석)을 했었다. 왜냐하면 문자열이라 그대로 사용할 수 없었기 때문에.

- 비록 문자열이지만 키:값 형태로 되어있기 때문에 각각 언어별 키:밸류 데이터 타입으로 파싱할 수 있다.



카카오로 로그인, 구글로 로그인같은건 해당 사이트의 REST API 활용한 것.



문서를 응답하는 형태 == 평소에 항상 사용하던 형태



Json 함수 => JsonResponse라는 함수를 사용함. 반복문을 통해 article.json



__Serialization__

직렬화 : 데이터 구조나 객체 상태를 동일하거나 다른 컴퓨터 환경에 저장하고, 나중에 재구성할 수 있는 포맷으로 변환하는 과정

Queryset이나 Model Instance과 같은 복잡한 데이터를 JSON, XML 등의 유형으로 쉽게 변환할 수 있도록 __Python__ 데이터 타입으로 만들어줌

쿼리셋 ---> python 데이터 타입(직렬화) ---> JSON, XML 등등등...

예시로는 views.py 내 article_json_2를 확인하면 볼 수 있다.

```python
data = serializers.serialize('json', articles)
```

data => 직렬화된 객체(파이썬 데이터)!

근데 json2는 json1이랑 데이터 구성이 조금 다르다. model과 pk가 들어가 있고, 나머지 데이터들이 fields 안에 포함되어 있는 형태를 가지고 있다. 이는 serializers모듈의 serialize 메서드가 만들어준 것이다.



__장고 REST FRAMEWORK__

DRF 라이브러리를 사용해야 한다. 이를 위해

```bash
# pip install djangorestframework
```

__settings.py__

```python
INSTALLED_APPS = [
    'rest_framework',
]
```



many=True : 앞에 들어오는 객체( 여기서는 articles )가단일 객체가 아닐 때 써주는 옵션이다.



p.54~

원래는 html로 다 만들어줬었는데 실제로는 json형태로 보내주면 브라우저에서 열심히 그려서 출력하는 형태다. 왜냐하면 서버에 존재하는 데이터가 엄청나게 많기 때문에!!



```bash
from articles.serializers import ArticleListSerializer
serializer = ArticleListSerializer()
serializer

article = Article.objects.get(pk=1)
article

serializer = ArticleListSerializer(article)

serializers.data # 필요한 데이터들이 나온다...?

article = Article.objects.all()
serializer = ArticleListSerializer(articles)
```



--------------------



api_view decorator은 GET메서드만 허용함. DRF에서는 선택이 아니라 필수적으로 작성해야 한다. 해당 인자를 넣지 않으면 405 오류가 나온다.



Serializer에 두 종류의 Serializer 생성

views와 urls에 article_detail 관련 생성

__Multiple object를 조회하느냐 Single Object를 조회하느냐 차이__



elif를 사용하는 이유 : 각 HTTP method에 따라 뭐를 요청하는지 명확하게 구분하기 위해서!



```python
if serializer.is_valid(raise_exception=True):
```

 유효성 검사에서 오류가 났을 때 400 오류를 리턴하는 속성값
