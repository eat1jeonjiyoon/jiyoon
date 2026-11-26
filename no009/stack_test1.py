# Stack의 초기화
# index  0     1     2     3     4
stack = [None, None, None, None, None]
top = -1

# 스택 상태 출력(프린트 함수)
def print_stack():
    print("=== 스택 상태 ===")
# range(start,end,step): start 부터 end까지 step만큼 증가/감소
# for i in range(top, -1, -1):
    for i in range(len(stack) - 1, -1, -1): #len(stack)에서 -1을 한 이유는 index가 4까지라
        print(stack[i])
    print("================")

# Stack 초기화 함수
def init_stack(size):
    global stack, top
    stack = [None] * size
    top = -1
    return print("스택 초기화 완료! 스택의 크기: " + str(size))

# Push 함수
def push(data):
    global top
    top += 1
    stack[top] = data
    return print("현재 top: " + str(top))

def pop():
    global top
    data = stack[top]
    stack[top] = None
    top -= 1
    return print("Pop된 데이터: " + str(data) + ", 현재 top: " + str(top))


# Stack 초기화
init_stack(7)

print_stack()

# Push
push("커피")
push("녹차")
push("꿀물")
push("레몬차")
## -1 + 1 = top /데이터를 먼저 저장해야 pop에서 데이터를 안 잃어버림(?)
#top += 1
#stack[top] = "커피" #현재 top은 0임. index 0을 찾아가
#top += 1
#stack[top] = "녹차" #현재 top은 1임. index 1을 찾아가
#top += 1
#stack[top] = "꿀물" #현재 top은 2임. index 2을 찾아가

print_stack()
#print("=== 스택 상태 ===")
## range(start,end,step): start 부터 end까지 step만큼 증가/감소
## for i in range(top, -1, -1):
#for i in range(len(stack) - 1, -1, -1): 
#    print(stack[i])

# Pop
pop()
#data = stack[top] #데이터 저장
#stack[top] = None #None으로 초기화
#top -= 1
#print(f"Pop된 데이터: " + str(data))

print_stack()
# print("=== 스택 상태 ===")
## range(start,end,step): start 부터 end까지 step만큼 증가/감소
## for i in range(top, -1, -1):
# for i in range(len(stack) - 1, -1, -1): #len(stack)에서 -1을 한 이유는 index가 4까지라
#    print(stack[i])