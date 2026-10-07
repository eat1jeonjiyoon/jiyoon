# 전지윤
## 202630129

## 9월 10일(2주차)
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