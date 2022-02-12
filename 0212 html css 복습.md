현재의 웹 표준을 만든 곳은 2군데 : W3C와 WHATWG

WHATWG를 이루는 회사 4군데 = Apple, Google, Microsoft, Mozila

HTML : Hyper Text Markup Language

HTML은 비 선형적으로 이루어진 텍스트. 웹 페이즈를 작성(__구조화__)하기 위한 언어

구글 효과 : 기억력을 감퇴시키는 이유는 정보를 애써 기억하지 않고 필요할 때 찾으면 되기 때문. 그래서 생기는 건망증이 구글 효과(Google Effect)



__HTML 기본 구조__

```
html : 문서의 최상위 요소
head : 문서 메타데이터 요소
	문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
	일반적으로 브라우저에 나타나지 않는 내용
body : 문서 본문 요소
	실제 화면 구성과 관련된 내용
```



HEAD 예시

```
<title> : 브라우저 상단 타이틀
<meta> : 문서 레벨 메타데이터 요소
<link> : 외부 리소스 연결 요소(CSS 파일, favicon 등)
<script> : 스크립트 요소 (JavaScript 파일/코드)
<style> : CSS 직접 작성
```



__DOM(Document Object Model) 트리__

```
텍스트 파일인 HTML 문서를 브라우저에서 렌더링 하기 위한 구조
	HTML 문서에 대한 모델을 구성함
	HTML 문서 내의 각 요소에 접근 / 수정에 필요한 프로퍼티와 메서드를 제공함

parents 관계
sibling 관계
```



요소

```
태그(Element, 요소)는 콘텐츠(내용)를 감싸는 것으로 그 정보의 성격과 의미를 정의
내용이 없는 태그들
	br, hr, img, input, link, meta
요소는 중첩될 수 있음
여는 태그와 닫는 태그의 쌍이 이상할 때는 오류를 반환하는 것이 아닌 그냥 레이아웃이 깨진 상태로 출력되기 때문에 디버깅이 힘들어질 수 있다.
```



속성

```html
<a href="https://google.com"></a>
```

__공백을 사용하면 안되고, 무조건 주소에 쌍따옴표 써야 한다__

__요소의 시작 태그에 작성하며, 보통 이름과 값이 하나의 쌍으로 존재한다__

태그와 상관없이 사용 가능한 속성(HTML Global Attribute)들도 있다.



HTML Global Attribute

```
모든 HTML 요소가 공통으로 사용할 수 있는 대표적인 속성
	id : 문서 전체에서 유일한 고유 식별자 지정
	class : 공백으로 구분된 해당 요소의 class 목록(CSS, JS에서 요소를 선택하거나 접근)
	data-* : 페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용
	style : inline 스타일
	title : 요소에 대한 추가 정보 지정
	tabindex : 요소의 탭 순서
```

