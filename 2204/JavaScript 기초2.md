for ... in

예시에는 capitals에 뭐시기뭐시기 나와있는데 이거보다는 객체의 속성을 조회할 때 사용한다고 이해하면 편함

- 사람 ( 객체 )
  - 이름
  - 키
  - 생일
  - 성별



p.82

```js
const f = func() {
    
}

func(func())

return func()
```



p.92

```js
const greeting = function (name = 'Anonymous') {
    return `Hi ${name}` // `` 물결표시 쉬프트 안누른거
}

greeting()
'Hi Anonymous'
```



p.112

replace는 첫 번째로 나오는거만 바꿔준다.

전부 다 바꾸고 싶으면 replaceAll 사용



115

파이썬이랑 다르게 -1 인덱스로 접근하면 undefined가 나옵니다.

```js
const numbers = [1, 2, 3, 4, 6]

console.log(numbers[0]) // 1
console.log(numbers[-1]) // undefined
console.log(numbers.length) // 그냥 길이 반환 => 5
```



117

```js
number.reverse() // numbers 배열 자체를 바꿔버림!
```



122

join() -> default는 콤마. 원래 그렇게 돼있었으니까?





```js
const numbers = [1, 2, 3, 4, 5]
doubleNum = numbers.map((number) => number*2)
```



128

```js
const numbers = [1, 2, 3, 4, 5]
const oddNumber = numbers.filter()
```



130

```js
numbers.reduce( function, initialValue )

const result = numbers.reduce( (acc, number) => acc + number, 0)
```



135

break와 continue는 사용이 불가능하다. 왜냐하면 전부 다 반복할거니까!



136

getFullName 형태로 부르면 함수가 return됨

getFullName() // 함수니까 이런식으로 호출해줘야함



158

Loadsh.com 접속 -> 설치 안하고 docs 들어가서 cdn으로 사용할 수 있음.