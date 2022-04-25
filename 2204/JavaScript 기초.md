



DOM과 BOM을 조작하기 위해서는 JavaScript Core가 필요하다. => ECMAScript(js)



p.12~

HTML을 프로그래밍으로 조작할 수 있다!

p.15 예시를 보며, 프로그래밍으로 어떻게 HTML을 조작하는지 확인할 수 있다.



구글 브라우저 -> 개발자 도구 -> Console

```javascript
console.log(1)
```



- 오른쪽 버튼 -> clear console : 선언한 변수 그대로 남아있음
- 새로고침 -> 선언한 변수 전체 없어짐



__const의 경우, 재할당이 불가능하다__



__재선언은 let과 const 둘 다 불가능하다__

chrome에서 재선언이 가능한 것처럼 보이는데, 오타날까봐 undefined가 뜨지만, 원칙적으로 불가능!

```javascript
const number = 10
const number = 20
```

```js
let number = 10
let number = 20
```



p.38~

블록 스코프 : 중괄호 내부 변수는 괄호 안에서만 변화한다.

```js
let x = 1

if (x === 1) {
    let x = 2
    console.log(x) // 2 출력
}

console.log(x) // 1 출력
```



p.39 ~

var로 선언한 변수는 __재선언과 재할당 모두 가능__하다! But 사용하지 않는 걸 권장한다.



p.42 호이스팅

```js
console.log(username)
var username = '홍길동' // 이처럼 선언부분이 출력부분보다 더 밑에있는 경우? undefined가 됨.
```

이처럼 선언 이전에 참조할 수 있는 현상!

변수 선언 이전에 위치에서 접근 시, undefined. 이런 문제가 뜨면, 진짜 undefined와 가짜 undefine를 구분하기 어렵다.



```js
console.log(username)
var username = '홍길동' // undefined

console.log(email)
let email = 'gildong@gmail.com' // let은 오류 발생!

console.log(age)
const age = 50 // const도 오류 발생!
```



__원시 타입과 참조 타입__

- 원시 타입 : 값을 복사
- 객체 타입 : 참조 값(주소값)을 복사

```js
let message = '안녕하세요!'

let greeting = message
console.log(greeting)

message = 'Hello, world!'
console.log(greeting)
```



p.51~

undefined => 개발자의 의도 X / 그냥 값이 없어! 아직 할당을 안했어!

null => 개발자의 의도 O / 값이 없음을 의도적으로 표현하고 싶을 때 사용



p.55~ 자동 형변환 규칙

NaN => Not a Number이라는 뜻!



p.58

```js
let num = 100
num += 1 // 101
num++ // 호출하고나서 +1 해줌
```

다만, Airbnb 스타일가이드에서는 __명시적이지 않다__는 이유로 +=나 -=를 사용할 것을 권장



p.59

알파벳 비교같은 경우, ASCII 값을 본다. 정확하게 말하면 유니코드를 비교하는 것.



p.60 동등 비교 연산자(안씁니다.) 이유는 다음과 같음

```js
0 == "0" // 이딴게 true로 나온다.
0 == [] // true
'0' == [] // 근데 이건 false ㅋㅋ 삼단논법이 안먹힘
```



p.61 __일치 비교 연산자__

- 엄격한 비교 ( __타입__과 __값__이 모두 일치하는지를 비교! )
- 암묵적 타입 변환 X



p.62 __논리 연산자__

- 웬만한 언어들은 거의 __&&, ||, !__를 사용한다.
- !'Bonjour'가 false인 이유는 __내용물이 있는 String값__을 not연산 했기 때문에!



p.68 __if statement__

- 조건에는 __소괄호__ 써주는거
- 실행할 코드는 __중괄호__
- elif나 else는 __끝나는 중괄호 옆!__에 써주기



p.70 __switch__

사용하는 이유 => nation 하나를 그냥 알고 싶은데 계속 비교해야되나...? 싶어서 사용

- __default__는 else와 같다고 이해하면 좋은 듯...?

- __break__를 써주지 않으면, 계속해서 코드를 비교하면서 내려간다.
- 특히, break를 쓰지 않으면 __참 조건 이후__는 전부다 출력해버리기 때문에 break를 써줘야합니다.
  - 조건에 맞으면 식에 입장한다는 느낌. 



p.75

- 파이썬의 for문은 __for...in__과 __for...of__쪽이 더 가깝다. 그냥 for은 불-편한 for

```js
if (true) {
    var a = 1
    let b = 2
    const c = 3
}

console.log(a) // 1 => var만 블록 안에 있는 걸 계속 가져갈 수 있다.
console.log(b) // undefined
console.log(c) // undefined
```

```js
i = 0
while (i < 3) {
    var a = 1
    let b = 2
    const c = 3
    i++
}
// 마찬가지로 var만 중괄호 밖에서 쓸 수 있음! 나머지는 안에서만 유효하다.
```



p.78

```js
for (let i=0; i<10; i++) { // i가 0으로 시작하고, i가 10보다 작다면, 끝날때마다 i에 1씩 더해준다.
    console.log(i)
}
```



p.80

자바스크립트에서 말하는 class의 instance가 아니라 __dict의 key__를 의미한다!

```js
const capitals = {
    korea: 'seoul',
    france: 'paris',
    USA: 'washington D.C'
}

for (let nation in capitals) {
    console.log('#{nation}의 수도는 #{capital[nation]}')
}
```



__in은 key값을 출력, of는 value 값을 출력!!!__

__for in의 대상은 Object, 객체 순회에 적합하고 for of의 대상은 Array, 배열 순회에 적합하다__



p.83 __let과 const 중 뭐가 좋은가?__

- value값을 재할당 할 일이 있다? => let 사용 가능.
- 무조건 그대로 가져갈거다 => const

```js
for (const fruit of fruits) {
    console.log(fruit + '!')
} // 이런식으로는 사용이 가능하다는 걸 기억하자! 왜냐하면 재할당이 아니기 때문에
```

근데 어지간하면 const로 쓰는 게 좋다. 진짜 생각보다 let을 쓰는 일이 __정~~~~말!!!__ 없는 편이다.