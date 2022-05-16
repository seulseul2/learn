p.13

스크립트를 다 보는 게 아니라 마크업만 본다



p.16

SSR은 장고 생각하면 편함



p.18

브라우저 == 클라이언트 == 여러분 컴퓨터

비용적인 측면에서는 CSR이 더 좋다.



p. 22 ~ 23

원래는 문서 전체(HTML)를 전송했었는데, 이제 JSON만 주고받으면서 브라우저한테 일을 많이 시킨다.

Template의 영역이 사용자한테 떠넘겨진 것(?)



p.35~p.36

```vue
<input> v-on:keyup.enter="onInputChange"
```

DOM과 Data가 연결되어 있어서, 내용을 입력하면 알아서 DOM조작이 된다.



p.41

Vue에서 Model은 자바스크립트 오브젝트다!

ViewModel은 데이터를 바꿨을 때 가운데에서 알아서 DOM조작을 해주는 친구!



vue CDN

```vue
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
```



```vue
<h2>선언적 렌더링</h2> // 애가 View
  <div id="app1">
    {{ message }}
  </div>

new Vue({ // 전체가 VM
  el: '#app1',
  data: { // 애가 Model
    message: '안녕하세요 Vue!'
  }
})
```



```vue
const obj = {
  el: '#app5',
  data: {
  message: '안녕하세요'
}
}
```

뭐 아무튼 여기에 function처리 꼭 해줘야함! () 괄호 써줘야 동작합니다.



토글 = true와 false를 왔다갔다 한다는 얘기

v-show의 경우, false일 경우 __있기는 한데 안보이게 만들어놨다__

