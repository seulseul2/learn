__HTML 복습__

1. form action=" "
   연결하는 url을 위한 명령어입니다. 뒤에 method를 붙여주면 GET POST 등 어떤 방식으로 정보를 받아들일지 정할 수 있습니다.

1. label for=" "
   - label은 폼의 양식에 이름을 붙이는 태그입니다.
   - 주요 속성은 for입니다. label의 for의 값과 양식의 id값이 같으면 연결됩니다.
   - label을 클릭하면, 연결된 양식에 입력할 수 있도록 하거나 체크를 하거나, 체크를 해제할 수 있습니다.
2. input type=" " id=" " name" "
   - id는 중복으로 사용할 수 없으며, label 값과 연결하여 사용할 수 있다. 주로 자바스크립트에서 사용한다고는 하는데 아직 잘 이해는 가지 않는다.
   - name은 page영역에서 중복되어 사용이 가능하다는 특징이 있다. 차후에 파라미터의 key값으로 사용되는 것이 name에 저장한 변수, 그리고 input으로 들어온 값이 value가 된다고 이해하고 넘어가겠다.



app/templates 위치 정해주는 곳



views같은 경우는 사실 templates의 경로를 작성하는 것. 'dinner.html'도 앞에 articles/templates/dinner.html로 안쓰는것처럼 약속됨

base같은 경우도 {% extends 'base.html' %} 도 약속된 경로는 없었지만, DIRS에 [BASE_DIR / 'templates',],로 지정해준 것.



articles가 먼저 렌더링이 된 이유는?

index.html을 렌더링한다. -> 검색을 해서 만나는데 이 순서는 INSTALLED_APPS = [] 에 추가된 순서대로 확인한다.

이 문제를 해결하기 위해서 강제로 이름공간을 만드는 것. __어떤 앱의 URL인지 표시하기 위해서__

-> articles 내 urls.py에 urlpatterns 위에 app_name = 'articles'라고 이름을 지정해준다. 따라서 이를 불러올 때 articles:index로 불러옴

__참조는 ':' 연산자를 사용하여 지정__



__articles/templates 안에 articles라는 파일을 새로 만들어서 그 안에 html들을 복사 붙여넣기 해줍니다.__

articles/templates/index.html -> articles/templates/articles/index.html. 어차피 검색은 templates 뒤 articles/index.html로 하기 때문에 중복될 수가 없다. 이거는 view.py 함수에서 html 앞에 전부 articles/를 붙여주는 쪽으로 변경해주어야 한다.

마찬가지로 pages에도 templates 안에 pages라는 폴더를 만들고 그 안에 html을 넣어준다. 이후, view 함수에 들어가서 pages/ 붙여주기

+ 추가로 이 작업을 할 때, base.html에 참조하는 html의 경로를 재설정해 줄 필요가 있다. ( 동영상 내 articles/_nav.html 사례 )

