## 함수 선언 부분 ##
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

## 전역 변수 선언 부분 ##
G1, G3 = None, None

G1 = graph(4) #함수 호출(없으면 오류남)
# G1.graph[초코][딸기] = 1 처럼 한글로 작성하면 오류날 가능성 높음
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