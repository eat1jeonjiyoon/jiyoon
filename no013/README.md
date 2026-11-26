# 11월26일(13주차)

1. 재귀호출(Recursion): (다시 귀환)본인을 호출함
    - 콜백함수
    - 재귀 호출(함수)의 형태
2. 재귀 알고리즘: 양쪽에 거울이 서로 마주보니 거울 속에서 비침이 무한반복됨
    - 예) 마트료시카 인형
        - 동일한 작동을 무한적으로 반복함
---

- vs코드에서 막고 있어서 무한 반복(루프)을 볼 수 없다.
    - 무한 반복하면 종료 불가 리소스를 많이 잡아먹음 -> 오류
```python
def callback():
    print("Callback function executed")
    callback()

callback()
```

---
- 함수의 무한 루프를 종료시킬 수 있어야 한다.
```python
def callback():
    global count
    count -= 1
    if count == 0:
        print("Count reached zero. Stopping execution.")
        return
    print("Callback function executed")
    callback()

count = 10
callback()
```

---
- 매개변수 필수
```python
def callback(num):
    # global count
    num -= 1
    if num == 0:
        print("Count reached zero. Stopping execution.")
        return
    print("Callback function executed. count", num)
    callback(num)

callback(10)
```

---
- 1에서 10까지 더하기
```python
def add_numbers(num):
    if num <= 1:
        return 1
    else:
        return num + add_numbers(num - 1)

    print(add_numbers(900))
```

---
```python
def add_numbers(start, end):
    foo = start + end
    bar = foo + end
    woo = bar / 2
    print("woo:", woo)

add_numbers(1, 10)
```

---
- 연산 횟수를 줄임(좋은 알고리즘)
```python
def add_numbers(start, end):
    foo = ((start + end) * end) / 2
    print("foo:", foo)

add_numbers(1, 100000)
```

---
- 1을 호출하기 위해 // print("n:", n) // 사용
```python
def factorial(n):
    if n <= 1:
        print("n:", n)
        return 1
    print("n:", n)
    foo = factorial(n - 1)
    print("n:", n)
    return n * foo

print(factorial(5))
```

---
- 로켓 카운트다운
```python
# def countdown(n):
#     if n <= 0:
#         print("발사!!!")
#         return
#     print(n)
#     countdown(n - 1)

# countdown(5)

def countdown(n):
    for i in range(n, 0, -1):
        print(i)
    print("발사!!!")

countdown(5)
```

---
- ( * )을 이용해 삼각형 출력
```python
def print_start(n):
    if n <= 0:
        return
    print("*" * n) #역삼각형
    print_start(n - 1)
    print("*" * n) #삼각형

print_start(5)
```

---
- 각 단은 1부터 시작하니까 1은 상수임
```python
# def gugu(dan, num):
#     num = 1
#     if num > 9:
#         return
#     print(f"{dan} * {num} = {dan * num}")
#     gugu(dan, num + 1)

# gugu(2)

def multiplication_table():
    for i in range(1, 10):
        for j in range(1, 10):
            print(f"{i} x {j} = {i * j:2}")
        print()

multiplication_table()
```

---
- 피보나치 수열: 첫째 항과 두번째 항이 1임
    - 수열: 어떤 공식을 더한(1,2,3,4,5... 또한 수열임)
~~~
_____________________________________
|       |   2   |                   |
|   3   |_______|                   |
|_______|_1_|_1_|                   |
|               |                   |
|               |           8       |
|       5       |                   |
|               |                   |
|_______________|___________________|
1, 1, 2, 3, 5, 8, 13, 21
~~~
- 회문: 앞으로 읽으나 뒤로 읽으나 똑같음
    - 예) 우영우, 기러기, 스위스, 토마토, level, Borrw or rob(borr)
- 프랙탈(Fractal): 작은 부분이 전체와 비슷한 모양으로 끊임없이 반복되는 기하학적 구조 