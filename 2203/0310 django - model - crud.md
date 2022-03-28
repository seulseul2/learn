__Django 참조 구분__

```
: -> {% url 'articles:new' %} 을 쓸 때, appname:name 형태로 사용한다. 혹은 redirect하는 경우
. -> 인스턴스 변수. 보통 variable routing에서 { article.title } 이런식으로 사용
/ -> render 할 때, 'articles/new.html' 처럼 사용
```

