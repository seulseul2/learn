__DP 복습__

```python
# recursive(재귀)방식

def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
```

다만 이러한 방식은 타임 오버헤드가 일어난다. 왜냐하면 계속해서 같은 값을 반복 호출해주어야 하기 때문이다. 예를 들어, 위 함수의 경우 무수히 많은 fibo(2) 함수가 호출된다. 결국 return n이 되기 위해서 2보다 큰 숫자들은 모두 fibo(2)를 한번은 호출해야 하기 때문이다.



따라서 fibo(n)의 값을 계산하자마자 저장하면(memoization) 실행 시간을 O(n)으로 줄일 수 있다.

```python
def fibo(n):
    global memo # 전역변수 memo 사용
    if n >= 2 and len(memo) <= n: # n이 2보다 크고, memo의 길이가 n보다 작거나 같다면,
        memo.append(fibo(n-1) + fibo(n-2))
    return memo(n) # 이러한 방식을 통해 memo에 있는 값을 빠르게 가져올 수 있다.

memo = [0, 1] # 피보나치 수 0과 1 저장용
```

동적 계획(Dynamic Programming) 알고리즘은 입력 크기가 작은 부분들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결하여, 최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘.