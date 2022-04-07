__로켓 확인까지__

```bash
python -m venv venv # 가상환경 생성
```

```bash
pip install -r requirements.txt # 필요한 파일 설치
pip install django==3.2.12 # requirements 파일이 없는 경우!
```

```bash
django-admin startproject 프로젝트명 . # 프로젝트 생성
```

```bash
python manage.py runserver # 서버 실행
```



--------------------------



__프로젝트 기본 세팅__

```bash
python manage.py startapp 앱이름 # 앱이름은 보통 복수로 지정 +'s'
```

settings

- INSTALLED_APPS에 앱 추가 ( 반드시 생성 후 추가 )
- 필요하다면 LANGUAGE_CODE와 TIME_ZONE 설정
- 만약 공통 html 포맷을 상속받으려면 TEMPLATES => DIRS에 BASE_DIR / 'templates', + @

urls.py

- from django.urls import path, __include__ : include function 추가
  - path('앱이름/', include('앱이름.urls')),

__프로젝트 세팅 끝!__



-------------------



__html 기본 포맷__

- articles와 동일한 위치에 templates 폴더 생성
- 폴더 안에 base.html 파일 생성
- 파일 내 ! + tab 이용해서 기본 폼 만들어주고 bootstrap css 링크 + js링크 붙여넣기

```html
<div class="container">
    <% block content %>
    <% endblock content %>
</div>
```





-------------------



__DB(models)__

- models 모듈의 Model 클래스를 상속받는 Article 만들기

```python
class Article(models.Model):
    title = models.Charfield(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

- 설계도를 만들고, 반영

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```





-------------------------



__DB(forms)__

```python
from django.forms import ModelForm # django.forms 모듈의 ModelForm 클래스 import
from .models import Article # 동일 앱 내 models.py에서 생성해둔 Article 클래스 import
```

```python
class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
```







-------------------

__앱 세팅__

1. __urls.py__

   - admin은 따로 가져올 필요 없고, from django.urls import path만 가져오면 됨

   - app_name = '앱이름' 으로 설정해주기

   - urlpatterns = [] 해주고 페이지별로 path 만들어주기

     ```python
     path('링크 주소/', views.함수명, name=''), # 뒤에 쉼표 붙여주는거 잊지 말자
     ```





views 설계

메소드나 모듈을 가져올때는 .을 붙임

articles/index.html 은 파일 개념이기 때문에 /를 붙여줍니다.



index.html

articles/create 이름변경 귀찮을 수 있으니까, name='create' 해놔서 앞에 create/만 바꿔도 괜찮



create.html

POST로 보내주는 방법 + url 어디로 보내야하는지 + csrf token 설정 + input:submit 제출버튼

