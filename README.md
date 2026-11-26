# 전지윤
## 202630129
-------------------------------------------------------
# 11월 26일(13주차)

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

----
----
----
-------------------------------------------------------
# 11월19일(12주차)

1. 정점 = 노드
2. 간선,엣지 = 연결
---

- 그래프 구조
    - 방향 그래프: 간선에 방향(화살표)이 있는 그래프
    - 무방향 그래프: 간선에 방향(화살표)이 없는 그래프
    - 가중치 그래프: 간선 마다 가중치가 다르게 부여됨
    - 최소 신장 트리: 최소 간선으로 그래프의 모든 정점이 연결됨
    - 깊이 우선 탐색의 작동: 그래프의 모든 정점을 한 번씩 방문함(Graph Traversal)

- 그래프의 인접 행렬 표현: 자기 자신을 가리키는 엣지가 없으면 0.
    - 정점 그래프의 인접 행렬 초기 상태
~~~
        [A]                     _________________
                                | 0 |   |   |   |
[B]             [C]     ->      |   | 0 |   |   |
                                |   |   | 0 |   |
        [D]                     |   |   |   | 0 |
                                -----------------
~~~

---
- 그래프 정점 생성
```python
class graph():
    def __init__(self,size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

G1 = graph(4)
```

---
- 함수 선언 부분
```python
class graph():
    def __init__(self,size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

def print_graph(name, g):
    print("=== " + name + " 그래프 정보 출력 ===")
    for row in range(g.SIZE):
        for col in range(g.SIZE):
            print(g.graph[row][col], end="")
        print()
```
- 전역 변수 선언 부분
```python
G1, G3 = None, None
```
- 함수 호출(없으면 오류남)
```python
G1 = graph(4)
```
- //G1.graph[초코][딸기] = 1// 처럼 한글로 작성하면 오류날 가능성 높음
```python
G1.graph[0][1] = 1
G1.graph[0][2] = 1
G1.graph[0][3] = 1
G1.graph[1][0] = 1
G1.graph[1][2] = 1
G1.graph[2][0] = 1
G1.graph[2][1] = 1
G1.graph[2][3] = 1
G1.graph[3][0] = 1
G1.graph[3][2] = 1
print_graph("G1", G1)
# print("=== G1 무방향 그래프 ===")
# for row in range(G1.SIZE):
#    for col in range(G1.SIZE):
#        print(G1.graph[row][col], end="")
#    print()
```
```python
G3 = graph(4)
G3.graph[0][1] = 1
G3.graph[0][2] = 1
G3.graph[3][0] = 1
G3.graph[3][2] = 1
print_graph("G3", G3)
# print("=== G3 무방향 그래프 ===")
# for row in range(G3.SIZE):
#     for col in range(G3.SIZE):
#         print(G3.graph[row][col], end="")
#     print()
```

----
----
----
-------------------------------------------------------
# 11월12일(11주차)

- README통합
    - README를 한 README에 모아서 작성함
        - 예) 사용 설명서

---
- Queue 
    - front
    - rear
        - front = rear : 큐의 값이 비어있다
- 원형큐
    - (rear +1) -> 데이터 삽입
    - 하나 비어있다 : 꽉찬 상태
        - 예) (4 +1) % 5 -> 5 % 5 = 0 ##front와 같은 값이면 빈 값임.
        - 예) (1 +1) % 5 -> 2 % 5 = 2 ##front와 다른 값
```python
if((rear값 +1) % n == front값):
```

- 이진 트리(비선형 자료구조) : 나무가 꺼꾸로됨
~~~
_________________
      ↖ ↗
        |
        |
      ↙|↘
    ↙| | |
    ↙  ↘ ↘
        ↙| |
        | ↘
      ↙
~~~

---
```python
class tree_node:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

node1 = tree_node()
node1.data = "커피"

node2 = tree_node()
node2.data = "우유"
node1.left = node2

node3 = tree_node()
node3.data = "주스"
node1.right = node3

node4 = tree_node()
node4.data = "물"
node2.left = node4

node5 = tree_node()
node5.data = "콜라"
node2.right = node5

node6 = tree_node()
node6.data = "사이다"
node3.left = node6

print("=== 이진 트리 구조 ===")
print(node1.data, end="") # 공란없이(end="")
print()
print(node1.left.data, node1.right.data, end="")
print()
print(node1.left.left.data, node1.left.right.data, node1.right.left.data)
```

----
----
----
-------------------------------------------------------
# 11월5일(10주차)

- Stack, Queue</li>
- Stack:
    1. push
    2. pop
- Queue:
    1. EnQueue
    2. DeQueue

----
----
----
-------------------------------------------------------
# 10월29일(9주차)

- | FILO(선입후출) |
    - 스택(Stack): 한쪽 끝이 막혀 입구가 즉 출구라서 push(삽입)/pop(추출)/top(가장 위의 데이터(초기값: -1))
        - 예) 콘 아이스크림(콘과자 밑부분 초콜릿을 먹으려면 딸기->바닐라->커피 차례대로 먹어야됨/물론, 방법은 사람마다 다르겠지만 예를 들자면 그렇다.)
~~~
  (push)    딸기       ↑
    |       바닐라     |
    |       커피       |
    |       초콜릿     |
    ↓                (pop)
~~~

- | FIFO(선입선출) |
    - 큐(Queue): emgueue(넣기)/degueue(빼기)
        - 예) 입구> 4(딸기)->3(바닐라)->2(커피)->1(초코) >출구

```python
init_stack()
push()
pop()
is_stack_full()
is_stack_empty()
peek()
```

- 컴베이션
    - snake_case: 함수이름, 파일이름 등 전부 소문자 사용
    - kebab-case: snake_case와 같이 소문자를 사용하지만 다른점: -(마이너스)사용
    - PascalCase: 첫단어엔 대문자 사용
    - camelCase:  첫단어엔 소문자, 이후엔 대문자

---
프린터버퍼

웹브라우저: 파싱/파서(문서를 사람이 볼 수 있게 변화) | (stack) URL 히스토리 기능

- API
---

```python
import webbrowser
webbrowser.open("https://www.hanbit.co.kr")
```

---
인터프리터: 스크립트 컴파일
---

----
----
----
-------------------------------------------------------
# 10월22일(8주차)

중간고사

----
----
----
-------------------------------------------------------
# 10월15일(7주차)

<ol>
    <li>Pre / Head / Current</li>
        <ul>
            <ul>
                <li>단순연결리스트와 원형연결리스트 모두에 존재함</li>
            </ul>
            <li><h3 style="display: inline">Pre: </h3>Head의 이전 Node임.</li>
            <li><h3 style="display: inline">Head: </h3>첫번째 Node</li>
        </ul>
    <li>단순연결리스트</li>
        <ul>
            <li>첫번째 Node의 Link는 다음 Node가 없을 때, None이 들어감.</li>
            <li>마지막 Node의 Link가 없음(<a><s>Null</s></a>None)</li>
        </ul>
    <li>원형연결리스트</li>
        <ul>
            <li>첫번째 Node의 Link는 다음 Node가 없을 때, 첫번째,
            <br>즉, 본인을 가리키는 주소가 들어감.</li>
            <li>마지막 Node의 Link가 첫번째임.</li>
            <li>링크가 비어있으면 안됨.</li>
        <ul>
</ol>
<h2>원형연결리스트</h2>

~~~
예시) 다현--> 정연--> 쯔위--> 사나--> 지효-->
                |
               재남
~~~
<ol>
    <li>재남 Node의 Link에 정연 Node의 Link를 복사/붙여넣기.</li>
    <li>정연 Node와 재남 Node의 Link가 쯔위 Node를 가리키게 됨.</li>
    <li>정연 Node의 Link에 재남 Node를 연결함.</li>
</ol>
    <h3 style="display: inline">결과: </h3>정연 Node의 Link는 재남 Node를 가리키고, <br>재남 Node의 Link는 쯔위 Node를 가리키게 됨.

~~~
예시) 다현--> 정연--> 재남--> 쯔위--> 사나--> 지효-->
~~~

----
----
----
-------------------------------------------------------
# 10월8일(6주차)

1. #### 코딩글꼴(D2Coding)
    - 파이프(|), I, l, 1 / o, O, 0 / 언더바(_) 연속으로 사용하면 몇개인지 구분이 어려움.
    - 얼라인(맞춤)이 중요함(폭이 똑같다)

2. #### Node
    - head(첫번째)노드

        ▽(같이 붙어다님)
        - pre노드(current앞)
        - current노드(타겟(현재 처리중인 노드))
    - 과정(while(?))
        - head노드 생성 및 데이터 입력
        -> pre노드로 head노드를 참조
        -> 빈노드 생성(생성하며 메모리에 할당됨)
        -> 빈노드의 링크 연결
    ▶ Memory Leak: 기존 노드들과의 연결이 끊어짐(뒤쪽 데이터들을 잃어버림)(가비지)


~~~
pre = current
pre = link
~~~

### Node ▶ | data |[link]|
___
~~~
| current |[link]|-> | head |[link]|-> | C |[link]|-> | D |[link]|-> | E |[link]|
~~~

3. #### 원형 연결 리스트
    - 장점(?): 오버헤드 발생(X)
    - 단점: current 순서대로 찾음(삭제)

----
----
----
-------------------------------------------------------
# 10월1일(5주차)

~~~
1. 선형 리스트
    ▶단점: 시간복잡도(늘어날수록 그만큼 시간이 기하급수적으로 늘어남/삽입,삭제를 할 때)
2. 단순 연결 리스트
    ▶ Node: data와 link가 연결된 것
    ▶ link(주소)(None이 없으면 마지막 데이터(?))
    ▶ append
    ▶ 가비지 / 가비지 컬렉션
    ▶ 디스크 조각모음
    ▶ current노드는 첫번째 노드를 가리킴(?)
~~~

----
----
----
-------------------------------------------------------
# 9월24일(4주차)

추석

----
----
----
-------------------------------------------------------
# 9월17일(3주차)

 1. 선형 자료구조
 2. 비선형 자료구조
 3. 파일 자료구조:
    ▶ 순차 파일
    ▶ 직접 파일
    ▶ 색인 파일

4. 알고리즘 표현 방법
5. 설치 확인 방법(버전):
    ▶ --version
    ▶ -v
    ▶ 간혹 있는 경우( --v / -version )

----
----
----
-------------------------------------------------------
# 9월10일(2주차)

### 마크다운 문법
# h1 태그
## h2 태그
### h3 태그
...
###### h6 태그

~~~
*이텔릭체*

**볼드체**

***이텔릭+볼드***

~~취소선~~
~~~
밑줄
---
***

1. 감자
2. 옥수수
3. 배추


* 감자
* 옥수수
* 배추
    * 배추 김치
        * 신김치
            * 여기서 부터는 같음.

### 코드 블럭
```java
public class HelloWorld {
    public static void main(String[] args) {
        // 화면에 문장을 출력합니다
        System.out.println("Hello, Java!");
        
        int age = 20;
        String name = "홍길동";
        
        System.out.println(name + "의 나이는 " + age + "살입니다.");
    }
}
```

```py
# 화면에 문장을 출력합니다
print("Hello, Python!")

# 변수 선언 (데이터 타입을 자동으로 지정합니다)
age = 20
name = "홍길동"

# 문자열 포맷팅을 사용한 출력
print(f"{name}의 나이는 {age}살입니다.")
```

복사는 `ctrl+c` 입니다.

### 링크
(괄호 안에 주소 작성, "호거함.")
[구글 바로가기](https://google.com "구글 사이트")

(괄호 안에 #을 하면 ?전에 한거 나옴?)
[코드 블럭](#코드-블럭 "코드블럭 예제")

느낌표는 외부 링크가 아닐때(?)[이건 로딩중일때 표시할 이름?]
괄호 주소에 상위.. 을 하면 이미지가 취소?된 것 처럼 보임

![깃 로고](./image.png "git logo")

![깃 로고](../image.png "git logo")

----
----
----
-------------------------------------------------------
# 9월3일(1주차)

공부한 내용 요약