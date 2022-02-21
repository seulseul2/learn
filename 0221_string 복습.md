```
# 0x30 : '0' : 48 : 00110000
# 0x41 : 'A' : 65 : 01000001
# 0x61 : 'a' : 97 : 01100001
```

ord : 문자를 정수로 바꾸는 함수 ( 문자 -> 아스키 코드 )

chr : 정수를 문자로 바꾸는 함수 ( 아스키코드 -> 문자 )

----------------

__문자열을 뒤집는 2가지 방법, 특히 2번째 방법을 익혀두기__

```python
def myReverse(strV):
    word = ''
    for i in range(len(strV)-1, -1, -1):
        word += strV[i]
    return word

def myReverse1(strV):
    listV = list(strV)
    N = len(listV)
    for i in range(N//2):
        listV[i], listV[N-1-i] = listV[N-1-i], listV[i]

    result = ''.join(listV)
    return result
```

------------

__itoa(정수 -> 문자열)__

```python
def itoa(value):
    if value < 0:
        isMinus = True
        value *= (-1)

    strV = ''
    while value>0:
        r = value%10
        value = value//10
        t = chr(r + ord('0'))
        strV = t + strV

    if isMinus:
        strV = '-' + strV
    return strV
```

---------

__atoi(문자열 -> 정수)__

```python
```

--------

__index 함수 구현__

```python
t = 'This is a book~!'
p = 'is'

# patter이 text에 처음 나타난 위치를 return 합니다.
# pattern이 없으면 -1을 return
def Bru(pattern, text):
    N = len(text)
    M = len(pattern)
    i = j = 0

    while i<N and j<M:
        if text[i] != pattern[j]:
            i = i - j + 1
            #i = i + 1
            j = 0
        else:
            i += 1
            j += 1
    if j==M:
        return i-j
    else:
        return -1

print(Bru(p, t))
```

----------

