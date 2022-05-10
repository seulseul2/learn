__components__

한 화면을 구성하는 여러 컴포넌트. 처음에는 개발하면서 시간 소요가 증가하지만, 이후에는 변수 관리가 용이하며 기능별로 유지 & 보수 비용이 감소한다! 우리가 new Vue() 이렇게 하나하나 만드는게 모두 컴포넌트. 쪼개서 부품으로 조립하는 방식이구나!



__Vue 설치__

```bash
$ npm install -g @vue/cli
```

근데 __'-g'__는 설치에서 쓰라고 돼있을 때만 써줘야된다. 



__버젼 확인__

```bash
$ vue --version
```



__앱 생성__

```bash
$ vue create my-first-app

2번째꺼 선택
```



__서버 가동__

```bash
$ cd my-first-app
$ npm run serve
```

서버 끄는 방법 = ctrl + c



__Babel이란?__

- 자바스크립트의 최신 코드를 이전 버전으로 번역해주고, 변환해주는 도구. 몇몇 브라우저들은 업데이트가 돼있지 않아서 최신식 자바스크립트 문법(화살표 함수같은거..)를 이해하지 못하기때문에 번역해주어야 한다.



__Bundler이란?__

- 모듈 간 의존도를 낮추기 위해서, 카테고리별로 정리해주는 도구 정도로 이해하고 넘어가세요.



----------------------



SPA라고 부르는 이유? : vue에서 사용자가 보는 화면은 결국 index.html 하나기 때문에!



__canvas에 해당하는게 App.vue__ 나머지 조각조각들은 모두 components에 vue파일로 존재한다.

package-lock.json에서 우리가 필요한 것들을 알아서 설치해준다.



__구성요소__

- 템플릿(HTML)
- 스크립트(JavaScript)
- 스타일(CSS)



보여주기 부분에서 2가지 형태로 표현할 수 있다.

__카멜 케이스__

```vue
<TheAbout />
```

__케밥 케이스__

```vue
<the-about></the-about>
```



--------------------------



__App.vue__

```vue
<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <!-- 3. 보여주기 (print) -->
    <!-- 카멜 케이스 -->
    <!-- <TheAbout my-message="parentData"/> -->
    <!-- 케밥 케이스 -->
    <!-- ':'를 통해 바인드를 걸어줘야만 문자열이 아닌 함수로 받아들인다 -->
    <the-about 
      :my-message="parentData"
      @child-input-change="parentGetChange"
    ></the-about>
  </div>
</template>

<script>
// 1. 불러오기 (import)
import TheAbout from './components/TheAbout.vue'

export default {
  name: 'App',
  // 2. 등록하기 (register)
  components: {
    TheAbout,
  },
  // 데이터는 무조건 함수로 만들어야 한다.
  data: function () {
    return {
      parentData: 'This is parent data to child component'
    }
  },
  methods: {
    parentGetChange: function (inputData) {
      console.log('Boss: 들리는군..', inputData)
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
```



__TheAbout.vue__

```vue
<template>
  <!-- template 안에는 반드시 하나의 Element만 있어야 한다.. 그래서 div로 묶어주기  -->

  <div>
  <!-- props에 있는걸 data로 따로 처리 안해도 바로 쓸 수 있음 -->
    <h1>{{ myMessage }}</h1>
    <p>아하! div는 하나구나</p>
    <input 
      type="text"
      v-model="childInputData"
      @keyup.enter="childInputChange"
    >
  </div>

</template>

<script>
export default {
  name: 'TheAbout', // 개발자 도구 검사에서 컴포넌트 이름으로 나옴
  props: {
    // 키 이름 : 데이터 타입 형태로 정의
    myMessage: String, // my-message가 원래는 맞지만, -연산을 사용할 수 없으므로 myMessage
  },
  data: function () {
    return {
      childInputData: ''
    }
  },
  methods: {
    childInputChange: function () {
      console.log('Child!!', this.childInputData)
      // 부모 컴포넌트에게 1번인자 라는 이름의 이벤트를 발생 + 2번인자 데이터를 보냄
      // 첫번째 인자 = 이벤트 이름. 받는 쪽에서 @로 받아주게 된다. 두번째는 값
      // 케밥 케이스를 권장하는 이유 = 여기에 있는 이벤트명과 받아주는 @가 같아지기 때문에
      this.$emit('child-input-change', this.childInputData)
    }
  },
}
</script>

<style>

</style>
```

