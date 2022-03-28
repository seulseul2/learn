선택자(Selector) : h1같은거

content - padding - border - margin

block은 아래로 쌓이고

inline은 우측으로 쌓인다.

--------------

메타데이터 : 사진을 위한 데이터라고 이해하면 편함.



렌더링 : 어떻게 표현할지, 어떻게 만들지



DOM(Document Object Model) 트리



__중요__

br -> break line ( 개행, 줄바꿈 )

hr -> horizontal rule ( 수평선 )

img -> 링크로 표현하니까 내용 자체가 없을수밖에

input -> 입력값을 받기 위한 모양 ( link와 meta도 마찬가지 )



id, class, style 3개정도 많이 쓸 듯.



시맨틱 태그 -> div랑 기능상 차이는 없지만, html을 분석할 때나 구조화 할 때 더 유용하게 사용할 수 있다.



--------

텍스트 요소

b -> bold

i -> italic

em -> emphasis

----------------

이름을 눌러도 체크박스가 활성화되기 위해서는 label for이 뒤 'id'와 연결되어있어야 한다.

radiobutton은 name끼리 연결되어있어야 한다.

text같은 경우는 입력값이 value가 되지만, checkbox나 radiobutton은 value를 따로 설정해줘야 한다.

바로 들어가게 해주는 기능 -> autofocus.

----------------------------

__CSS__

CSS 정의 방법

인라인 -> 디버깅하기가 너무 어렵다. 10,000줄정도 되면 당연하게 찾기가 너무 어려움.



우선 순위

*(플랑크톤) -> div(요소, element) -> class -> ID Selector(#MyDiv) -> inline style(style="") -> !important

플랑크톤 -> 귀여운거 -> 생선 -> 상어 -> 항공모함 -> 핵폭탄

__class같은 경우는 나중에 선언된 것이 우선순위__