```bash
python -m venv venv
source venv/Script/activate
pip install django==3.2.12 djangorestframework django_extensions
pip freeze > requirements.txt
django-admin startproject django_back .
touch .gitignore # python, venv, django, vscode
python manage.py startapp accounts
python manage.py startapp articles
```



__settings.py__

```python
INSTALLED_APPS = [
    # local apps
    'accounts',
    'articles',
    # 3rd party apps
    'django_extensions',
    'rest_framework',
    
AUTH_USER_MODEL = 'accounts.User'
```



__accounts/models.py__

```python
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass
```



__articles/models.py__

```python
from django.db import models
from django.conf import settings

# Create your models here.

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```



__django_back/urls.py__

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/articles/', include('articles.urls')),
    path('api/v1/accounts/', include('accounts.urls')),
]
```



__urls.py__

```python
from django.urls import path
from . import views

app_name = '앱이름'

urlpatterns = [
    
]
```



```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```



articles 앱 내 serializers 폴더 만들어주고, 안에 모델  이름으로 article.py / comment.py 만들어주기



Serializer는 Models 내 데이터를 직렬화해 __보기 편한 Json형태__로 가공하는 것



__CORS__

8000번 포트에서 8001번 포트 요청을 보내면 브라우저에서 간섭하며 에러가 나온다.

서버는 응답을 보낸건 맞는데, 브라우저에서 안받아줌. => SOP (너무 중요한 내용입니다)

__http://store.compnay.com__ /dir/page.html

첫번째는 https 두번쨰는 81 세번째는 news.



----------------------------------------



다른 출처의 리소스를 불러오려면 올바른 COR header를 포함한 응답을 받아야 함

서버에서 헤더 포함시켜서 브라우저(클라이언트)한테 보냄. __막는건 클라이언트지만, 바꿔야 하는 건 서버!__



```bash
pip install django-cors-headers
```

INSTALLED APPS에 corheaders 추가

```python
INSTALLED_APPS = [
    'corsheaders',
]
```



__MIDDLEWARE의 경우, 필터 순서가 중요하다__

```python
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware', # 애보다만 위에있으면 됨.
]
```



CORS_ALLOWED_ORIGINS에 8000번 추가해주기

```python
CORS_ALLOWED_ORIGINS = [
    # Vue LocalHost
    'http://localhost:8000',
    'http://127.0.0.1:8001',
]

# 모두에게 교차출처 허용(*)
# CORS_ALLOW_ALL_ORIGINS = True
```



인증과 권한

Django에서 로그인(인증)을 했더라도, 다른 사람의 글까지 수정/삭제(권한)가 가능하지는 않음.



Basic Token Authentication

아이디와 비밀번호가 맞네? == authtoken_token(새로운 테이블)에서 token을 발급해주고 그 중 토큰을 클라이언트에 return! 해당 문자열(토큰)을 확인하면 어떤 사용자인지 알 수 있다.

이를 위해서 Request Header(요청 헤더) 내 Authorization 키에 토큰 값을 함께 보내준다.__Toekn 띄어쓰기 토큰값__



브라우저(로컬 스토리지)에 token 정보 저장. Request Header에 토큰과 함께 요청하면 __권한을 확인__



JWT는 바코드 형태라기보다는 __조영훈, 유효기간:2주, 인증__ 이라고 써있는 느낌이다. 그래서 __데이터베이스를 사용하여 토큰의 유효성을 검사할 필요가 없다.__ 다만, 탈취되었을 때 무효화가 불가능하기 때문에 유효기간을 매우 짧게 설정한다.



토큰의 경우, __데이터베이스 1개를 공유__하거나, __데이터베이스 당 토큰 1개씩 배정__하는 방법을 사용해야 함. 이를 해결하기 위해 JWT. __조영훈, 5분, 인증__ 형태로 들고가면 데이터베이스를 참조하지 않아도 되기 때문에 좋다.



```bash
pip install django-allauth
pip install dj-rest-auth
```



INSTALLED APPS에 추가해주고,

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}
```

```python
urlpatter = [
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
]
```



post맨으로 해본다면 ? POST형태로 전송 + raw 버튼 선택. JSON데이터로 전송

```bash
{
   "username": "admin",
   "password": "admin"
}
```

보내면 key라고 하는 토큰 값이 들어온 걸 확인할 수 있다. 또한, DB 내 authtoken_token에서도 확인 가능

이후, URL 통일성을 위해 이름을 바꿔준다. 이름은 겹쳐도 괜찮다.

```python
urlpatter = [
    path('api/v1/accounts', include('dj_rest_auth.urls')),
]
```



POST맨 주소 입력(POST방식) , Headers 체크, Key에 Authorization / Value에 Token__띄어쓰기__키값

이후, 테이블 내 토큰값이 사라진 걸 확인할 수 있다.



마찬가지로, settings.py와 urls.py를 수정한 뒤, POST맨 POST방식으로 signup을 보내기

dj-rest-auth 페이지 참조 https://dj-rest-auth.readthedocs.io/en/latest/installation.html

Body -> raw + Json

```json
{
    "username": "neo",
    "password1": "qwer123",
    "password2": "qwer123"
}
```

적어주면 Token 발급까지 만들어서 발급을 해준다!



accounts에 profile url과 view 만들어주고, serializers 파일 생성해서 ProfileSerializer 생성



``` python
from rest_framework import serializers
from django.contrib.auth import get_user_model
from articles.models import Article


class ProfileSerializers(serializers.ModelSerializer):
    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('pk', 'title',)
    like_articles = ArticleSerializer(many=True)
    articles = ArticleSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'email', 'like_articles', 'articles',)
```

이렇게 설정해주면, pk:1, title:뭐시기~ 이런 식으로 출력해준다. content를 출력해주고 싶으면 ArticleSerializer 안에 content도 추가해주면 됩니다! 이것은 결국, 한번에 데이터베이스에서 원하는 데이터를 가져와버리기 위한 작업입니다.



기존에 @login_required 를 사용했었는데 이게 없다.

- 모든 사용자에게 허용을 걸어놨기 때문

  ```python
  'DEFAULT_PERMISSION_CLASSES': [
      'rest_framework.permissions.IsAuthenticated'
  ]
  ```

  이렇게 바꿔주면 로그인한 사용자들만 이용 가능하도록 바뀐다...!

  이후에는 key에 Authorization / Value에 토큰 값이 없으면 토큰 값 없다고 정보 제공 안해줍니다.

  대신, signup과 login만큼은 로그인 없이도 접근이 가능하도록 만들어져있다.(알아서)