XML은 약간 HTML처럼 태그 여러개있는 스타일 -> 데이터의 양이 많다.

JSON은 진짜 객체 안에 속성들만 들어가있는 스타일



Ajax의 예시 -> 연관검색어

Network 탭에서 보면 실시간으로 search에 input을 넣을때마다 즉각적인 변화

-> preview에 들어가보면 새로고침 없이 실시간으로 데이터를 받아오고 있음. 이게 Ajax!



```js
const request = new XMLHttpRequest()
const URL = 'https://jsonplaceholder.typicode.com/todos/1'

request.open('GET',URL)
// request.send()

// const todo = request.response
// console.log(todo)

// 한줄씩 하는거랑 한방에 하는거랑 차이 O
```



__비동기식__

- 요청을 보내고 응답을 기다리지 않고 다음 코드가 실행된다. 위 코드 중

  ```js
  const request = new XMLHttpRequest()
  const URL = 'https://jsonplaceholder.typicode.com/todos/1'
  
  request.open('GET',URL)
  ```

  여기까지는 동기식

  ```js
  request.send() // 애는 문제가 XMLHttpRequest 요청하는데 응답이 올때까지 기다리는게 아니라 알아서 해! 해버린다음에 그냥 다음코드로 넘어가버림. 이 코드가 문제인거!!
  
  const todo = request.response // 아직 응답이 안넘어왔기 때문에 빈 값을 todo 선언&초기화
  console.log('data: ${todo}') // 열어볼까? 했는데 빈박스임.. 왜냐하면 응답이 아직 안와서
  ```



__비동기를 사용하는 이유?__

- JavaScript는 single threaded

- 데이터가 매우 클 경우, 데이터를 불러오는 동안 렉걸린것처럼 보임
- 비동기식 코드 -> 데이터를 받아오는 동안에도 앱 실행이 이뤄져 훨씬 쾌적한 사용자 경험



__Call Stack__

- 요청이 들어올 때마다 해당 요청을 순차적으로 처리하는 Stack(LIFO)형태의 __자료 구조__

__Web API__

- 브라우저 내부의 고마운 친구들(식기세척기, 세탁기..)

- 모든 일들을 대신해주는 것은 X
- __Ajax 요청 보내기, 시간 관련된 것__들 대신해줌. 이 두 가지 공통점은 __언제 끝날지 모름__

__Task Queue__

__Event Loop__



p31

setTimeout(콜백함수, 3000__<밀리세컨 단위, 3초 후에 어떤 일을 할거야>__)

```js
console.log('start') // 1

function after3Seconds() {
    console.log('3초가 지났나보군...') // 3
}

setTimeout(after3Seconds, 3000)

console.log('end') // 2
```



__왜 3초 뒤에 하는거는 Web API가 하는가?__

- 만약에 웹이 이걸 해버리면, 브라우저가 이벤트캐치를 아예 못하고 뻗어버리기 때문
- 왜냐하면 쓰레드 하나는 일 1개밖에 하지 못하기 때문에, 시간을 계속 계산하고 있어야 함



근데? 0초를 넣어도 시간 순서는 똑같다. 왜냐하면 __Call Stack이 빌때까지 Task Queue에 남아있어야 하기 때문__ 

그래서 Web API -> Task Queue에 갔다 오는 친구들은 우선순위가 무조건!!!! 더 낮다.



----------------------------



콜백 함수는 __즉시 실행되지 않고__ 함수의 body에서 때가 되면 실행됨!

그래서 장고에서도 url이 들어오면 -> views.??? // JS에서는 특정 이벤트가 발생하면 -> ??? 이런 식으로 사용



__Promise__

다짐식 코드를 의미!! 사실 이전에 피라미드와 다를 건 없지만, 가장 큰 차이점은 __들여쓰기가 같다__는 점 ( 외적으로 개선되었음 - 가독성 )



p.60 여기서 말하는 성공 결과 -> return값. 이걸 인자로 받음



__Axios__

Promise based HTTP client for the browser

single thread -> event loop & browser -> Async -> callback -> promise -> Axios



Axios 공식 문서 -> CDN 사용하기에 있는 코드 두개 중 아무거나 가져와서 body 안에 삽입해주기

```js
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
```

그 다음 URL은 jsonplacehorder에서 그냥 가져온거

```js
const URL = 'https://jsonplaceholder.typicode.com/todos/'
```

Promise 리턴하기

```js
axios.get(URL)
```

이후에는 response 데이터를 이어나가면서 .then을 사용할 수 있다.

catch에서 나오는 에러는 -> 에러 객체 전부를 가져오는 것. 여기서 response.status를 출력하여 뭐가 문제인지 확인할 수 있다.

finally 함수의 경우, 인자를 받지 않는다. 왜냐하면 실패했는지 성공했는지 알 수 없기 때문에!



05 코드 설명

1. 전체 종을 받아 옴

   ```js
   axios.get(URL + '/breeds/list/all')
   ```

   

2. 종 목록 중 첫 번째 종에 대한 이미지 받아오기

   ```js
   .then(res => {
       const breedObj = res.data.message // 강아지 데이터
       const breedArray = Object.keys(breedObj) // 강아지 이름(키) 데이터
       const breed = breedArray[0] // 강아지 목록 중 첫번째 강아지
       return axios.get(URL + `/breed/${breed}/images`) // 강아지 이미지 데이터 반환
   })
   ```

   

__async-wait 함수 작성__

```js
async function fetchDogImages() { // 앞쪽에 반드시 async를 적어주기
    const res = await axios.get(URL + '/breeds/list/all') // 비동기화되는 부분에 await
    const breedObj = res.data.message
    const breedArray = Object.keys(breedObj)
    const breed = breedArray[0]
    const images = await axios.get(URL+ `/breed/${breed}/images`) // 순서가 보장X await
}
```

++ 마지막으로 catch부분은 함수 뒤쪽에 써주어야한다.

```js
fetchDogImages()
  .catch(err => console.error(err))
```



Ajax의 핵심은 __인간 중심으로 설계된 사용자 경험!__