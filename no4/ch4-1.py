class Node:
    def __init__(self): #(self, data)으로 사용하면, 입력하는 것(?)이 데이터라는 것을 알림.
        self.data = None
        self.link = None

# 노드 생성. 첫 번째 노드라서 link는 None으로 설정.
node1 = Node() #node1 = Node("다현")으로도 사용 가능함.
node1.data = "다현"

node2 = Node()
node2.data = "정연"
node1.link = node2

node3 = Node()
node3.data = "쯔위"
node2.link = node3

node4 = Node()
node4.data = "사나"
node3.link = node4

node5 = Node()
node5.data = "지효"
node4.link = node5
#node5는 마지막 노드라서 link없다(?)

print(node1.data, end=', ')
print(node1.link.data, end=', ')
print(node1.link.link.data, end=', ')
print(node1.link.link.link.data, end=', ')
print(node1.link.link.link.link.data, end=' ')
#node1.다음으로 적혀진 link가 node2의 데이터 이고, 다음 link가 node3의 데이터임.
#그래서, node1.link(node2).link(node3).link(node4).link(node5)인 것.
#근데 이렇게 쓰면 노드가 많아질때 복잡해짐.

#24시간 돌림(?): for문 / 언제 끝날지 모르는, 입력받을 때 까지 기다림: while문
print("\n\n연결리스트 출력")
current = node1
print(current.data, end=', ')
while current.link is not None: # is not None을 != None로도 사용 가능함.
    current = current.link
    print(current.data, end=', ')
print(current.data)

####

new_node = Node()
new_node.data = "재남"
new_node.link = node3
node2.link = new_node

print("\n\n연결리스트 출력")
current = node1
print(current.data, end=', ')
while current.link is not None: # is not None을 != None로도 사용 가능함.
    current = current.link
    print(current.data, end=', ')

node2.link = node3
del(new_node) #python은 객체 자체를 메모리에서 지워주진 않음(?)
print("\n\n연결리스트 출력")
current = node1
print(current.data, end=', ')
while current.link is not None: # is not None을 != None로도 사용 가능함.
    current = current.link
    print(current.data, end=', ')