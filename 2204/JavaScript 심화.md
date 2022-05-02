p.37

윈도우가 의미하는 것 === 탭! ( 콘솔도 당연히 윈도우 안에 있는 거 )

도큐먼트 === 윈도우 안쪽에 흰색 부분!!

js는 window는 굳이 작성하지 않아도 생략 가능하게끔 설정되어있음! document === window.document



__Element.setAttribute(name, value)__

name에는 속성, ex) class 같은거

value에는 만들어둔 개별 클래스 이름 넣어주면 됨.

```js
footer.setAttribute('class', 'box-container footer')
footer.classList.add('footer') // 이런식으로도 클래스 추가 가능
```



Focusevent => 사용자가 어디에 마우스를 올려놨는지?



listner에

```js
const add = (x, y) {
    return x + y
}
```

이걸 listner에 넣는거. 실행이 아니라 명세를 정의하는곳임



```js
const alertMessage = function () {
      alert('메롱!!!')
    }

myButton.addEventListener('click', alertMessage)
myButton.addEventListener('click', alertMessage())
```

이거 두개는 진짜 엄청 다른거임!! 아래꺼는 return값이 없으니 undefined랑 똑같은 셈!!



prevent 개념 : click을 막는 게 아니라, 클릭을 했을 때 일어나는 사건(여기서는 체크되는거)을 막는거



event.target ==> .addEventListener 앞에 붙은거. 누가 event.target을 묻거든 주어를 보게하라...ㅋㅋㅋ

