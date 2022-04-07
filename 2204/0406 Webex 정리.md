__Webex__

중요했던 것

- 클라이언트 : 웹 브라우저를 띄워서 url을 서버(django)로 보냄
- 서버 : urls.py를 해석을 해서 view.py 파일과 연결. dtl언어가 포함이 돼서 만들어준다. 아무튼 구조 말씀..

----------

중간중간에 주석으로 설명 적어두었음.

----------------

```bash
python manage.py makemigrations
```

해당 명령어를 입력하면, 설계도를 생성하고, migrations 안에 0001 파일이나 0002파일이 생성된다.

이거는 파일 db.sqlite3에서 opendatabase를 입력하면 아래 메뉴줄에서 SQLITE EXPLORER에서 확인할 수 있다. ++ article_article에 들어가면 DB가 만들어졌음을 확인할 수 있다.

----------

new를 form을 사용하지 않았을 때는 form을 사용하지 않았고, context 참조도 하지 않았음

form 주석처리하고 기존 주석처리 지워주면 원래 form으로 복구 가능

어차피 django 프레임워크 내에서 데이터 처리 다 하니까 구조화된 양식을 사용하고 싶다 -> modelform