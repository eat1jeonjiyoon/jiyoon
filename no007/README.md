# 전지윤
## 202630129

# 10월 15일(7주차)

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
