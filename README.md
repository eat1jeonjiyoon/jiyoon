
------------------------------------
# 전지윤
## 202630129

# 11월5일(10주차)

<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>11/05</title>
</head>
<body>
    <div>
        <ul>
            <li>Stack, Queue</li>
            <li>Stack:
            <ol>
                <li>push</li>
                <li>pop</li>
            </ol>
            <li>Queue:
            <ol>
                <li>EnQueue</li>
                <li>DeQueue</li>
            </ol>
        </ul>
    </div>
</body>
</html>

--------------------------------------
# 전지윤
## 202630129

# 10월29일(9주차)

<ul>
    <li>|FILO(선입후출)|</li>
    <li>스택(Stack): 한쪽 끝이 막혀 입구가 즉 출구라서 push(삽입)/pop(추출)/top(가장 위의 데이터(초기값: -1))</li>
        <ul>
            <li>예) 콘 아이스크림(콘과자 밑부분 초콜릿을 먹으려면 딸기->바닐라->커피 차례대로 먹어야됨/물론, 방법은 사람마다 다르겠지만 예를 들자면 그렇다.)</li>
        </ul>
</ul>
<table>
    딸기
    바닐라
    커피
    초콜릿
</table>

<ul>
    <li>|FIFO(선입선출)|</li>
    <li>큐(Queue): emgueue(넣기)/degueue(빼기)</li>
        <ul>
            <li>예) 입구> 4(딸기)->3(바닐라)->2(커피)->1(초코) >출구</li>
        </ul>
</ou>

<ol>
    <li>init_stack()</li>
    <li>push()</li>
    <li>pop()</li>
    <li>is_stack_full()</li>
    <li>is_stack_empty()</li>
    <li>peek()</li>
</ol>

<ul><li>컴베이션</li></ul>
<ol>
    <li>snake_case: 함수이름, 파일이름 등 전부 소문자 사용
    <li>kebab-case: snake_case와 같이 소문자를 사용하지만 다른점: -(마이너스)사용
    <li>PascalCase: 첫단어엔 대문자 사용
    <li>camelCase:
</ol>

~~~
프린터버퍼

웹브라우저: 파싱/파서(문서를 사람이 볼 수 있게 변화) | (stack) URL 히스토리 기능

API

import webbrowser
webbrowser.open("https://www.hanbit.co.kr")

인터프리터: 스크립트 컴파일
~~~

-----------------------------------------
# 전지윤
## 202630129

# 10월22일(8주차)

중간고사

----------------------------------------
# 전지윤
## 202630129

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

----------------------------------------
# 전지윤
## 202630129
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

-------------------------------------
# 전지윤
## 202630129

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

---------------------------------
# 전지윤
## 202630129

# 9월24일(4주차)
추석

---------------------------------
# 전지윤
## 202630129

# 9월17일(3주차)

~~~
#1. 선형 자료구조
#2. 비선형 자료구조
#3. 파일 자료구조
    ▶ 순차 파일
    ▶ 직접 파일
    ▶ 색인 파일

#4. 알고리즘 표현 방법
#5. 설치 확인 방법(버전)
    ▶ --version
    ▶ -v
    ▶ 간혹 있는 경우( --v / -version )
~~~

----------------------------
# 전지윤
## 202630129

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

----------------------
# 이름
## 학번

# 9월3일(1주차)

공부한 내용 요약