__URL -> VIEW -> TEMPLATES__

데이터의 흐름에 맞추기 위해서



1. 가상환경 생성 및 활성화
2. django 설치 / pip install django==3.2.12
3. 프로젝트 생성 
4. 서버 켜서 로켓 확인하기
5. 앱 생성
6. 앱 등록



__부트스트랩 상속하는 방법__

{% extends '부모템플릿 이름' %} + block



원래 templates 위치는 app 내 templates에 저장했다.



settings.py에 들어가서 teplates = [] 에 보면 DIR: [] 라는게 있다. 여기에 추가 경로를 등록해야 한다.

먼저, 최상단에 templates를 만들고 그 안에 base.html을 만든다.

그 다음에 dir 내 경로를 추가할건데 BASE_DIR / 'templates',

BASE_DIR => 장고 프로젝트를 포함하고 있는 최상단 폴더.

절대경로를 사용하지 않는 이유는, 운영체제에 따라 달라질 수 있기 때문에 파이썬의 객체지향적인 특성을 이용하는 것이다.



__상속하는 방법__

1. 위처럼 setting 내 DIR에 BASE_DIR / 'templates',를 추가해준다.
2. base.html 파일에 부트스트랩 CDN을 불러온다
3. navbar가 필요한 경우, 부트스트랩 navbar 코드 복사 붙여넣기 + {% block 블럭이름 %} 설정해준다.
4. 상속받을 html에 찾아가서 body 안쪽 쳐내고 block 안에 넣는다. 그리고 최상단에 {% extends 'base.html' %}



__BASE.HTML 파일 내 nav 뜯어내기__

1. articles 앱 내 templates 안에 _nav.html 파일 만들기
2. base.html 파일 내 body 안에 {% include '_nav.html' %} 여기서 _는 별다른 뜻은 없고 include되는 html임을 나타냄