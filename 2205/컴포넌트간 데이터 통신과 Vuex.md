```bash
vue add vuex
```

Yes



src(@)를 보면, store에 index.js가 생겨있다.



- state ( == data )
- getters ( == computed )

- mutations ( == change )
- actions ( == methods )



vuex 이후부터는 script가 매우 얇아질 것이다. vuex에서 끌어와서 쓰는 용도로만 사용하게 됨.



```vue
import TodoList from '@/components'~ // 여기서 @는 src를 의미하는 vue 전용 기호
```

실제로 ./~랑 뭐가 다르냐고 할 수 있지만, components 밖으로 나갔을 때 @/components만 참조가 가능하게 됨.



너무 중요하다보니 mutations 내 함수는 전부 다 대문자로 쓰는 경우도 있다.

이후에 actions에서 뮤테이션을 호출한다. 이게 굉장히 비효율적으로 보일 수도 있다. 호출하는 템플릿은

```vue
createTodo(context) {
  context.commit('CREATE_TODO')
}
```

이걸 줄인게

```vue
createTodo({ commit }) {
  commit('CREATED_TODO')
}
```



INPUT DATA를 받는 가장 쉬운 방법은 v=model로 받아주는거. 당연히 data() return 형식으로 먼저 정의해주기

인풋 인자명을 두번째 인자로 넣어주고, method에 템플릿을 정의해준다. 이후에는 actions에도 두번째 인자를 추가해줘야된다. 마찬가지로 commit과 mutation에도 두번째 인자로 추가해주기. 이름은 통일하는게 좋은듯?



TodoList에 추가하고, 데이터를 날리는 방법?

method 안에 todoTitle:''로 재할당 해주기



DELETE는 splice, CREATE는 add 메서드 사용

근데 props에 todo:Object라고 먼저 설정해줘야한다.

```vue
state.todos.push(newTodo)

const index = state.todos.indexOf(todoItem) // 인덱스를 먼저 찾고
state.todos.splice(index, 1)
```





--------------------------------



isCompleted를 true로 바꿔주기?



muetations 내 UPDATE_TODO_STATUS() 생성하기 -> 마찬가지로 actions에도 updateTodoStatus({ commit }) 생성



deleteTodo(todo) todo를 꼭 넘겨줘야 __실행할 때, todo를 같이 넘겨준다__



FE에게 필요한 것(UX 향상을 위해 필요한 역량) 배려심 + 공감능력. 다른 웹사이트 돌아다녀보고 많이 알아둘수록 내 것에 적용할 수 있다.



update 중 이미 완성한 일들만 뽑아내는 콘솔 명령어

```js
todos.filter(todo => { return todo.isCompleted })
todos.filter(todo => { return !todo.isComplted })
```



```vue
getters: {
  completedTodosCount(state) {
    return state.todos.filter(todo => {
	  return todo.isComplted
    }) // 길이를 알고 싶다면, 뒤에 .length를 붙여주면 그만임!
  }
}
```

이런 식으로 작성하면 todo 중 끝난 애들만 따로 뽑아내준다.



이걸 바로바로 반영하려면 ? action은 method로 치환됐으니, 마찬가지로 getters는 computed로 치환

computed에 해당 getters를 추가해준 다음, 위에 {{ computed에 추가해준 녀석 }} 사용.

