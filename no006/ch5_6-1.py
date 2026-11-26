#Node 클래스 정의
class Node:
    def __init__(self): #(self, data)으로 사용하면, 입력하는 것(?)이 데이터라는 것을 알림.
        self.data = None
        self.link = None
        # 메모리 안에 있는 주소는 우리가 알수는 없으니, link

def print_nodes(start):
    current = start
    if current == None: # is None도 가능함.
        return
    print(current.data, end=' ')
    while current.link != None: # is not None > != None
        current = current.link
        print(current.data, end=' ')
    print() # <- current.data

def insertNode(findData, insertData):
    global memory, head, current, pre
    current = head
    if current.data == findData:
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return

    node = Node()
    node.data = insertData
    current.link = node

# 전역 변수 선언
memory = [] #노드 저장(23번에 생성된 노드)
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

if __name__ == "__main__":
    node = Node() #노드 생성
    node.data = dataArray[0] #첫 번째 노드에 데이터 저장
    head = node #head가 첫 번째 노드를 가리킴
    memory.append(node) #메모리에 노드 저장

    for data in dataArray[1:]: #두 번째 이후 노드
        pre = node #이전 노드 지정(?)
        node = Node() #새로운 노드 생성
        node.data = data #데이터 저장
        pre.link = node #이전 노드의 링크를 새 노드로 연결
        memory.append(node) #메모리에 노드 저장

    print_nodes(head) #연결리스트 출력

    insertNode("다현", "화사") #첫 번째 노드 앞에 삽입
    print_nodes(head) #연결리스트 출력
    insertNode("사나", "솔라") #중간 노드 앞에 삽입
    print_nodes(head) #연결리스트 출력
    insertNode("재남", "문별") #마지막 노드 뒤에 삽입
    print_nodes(head) #연결리스트 출력