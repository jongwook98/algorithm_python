# 순환선을 판단하는 기준은 check로 부터 다시 돌아왔을 경우 순환선으로 인식-> DFS 이용하는게 좋을듯?
# stack에 값을 저장해 놓은다음에 순환선을 발견한 그 구간부터 저장된 모든 구간 -> 순환선
# 갈 경로가 사라지면 stack에서 다시 pop 되니까!

# 어렵네,,,
# -> 순환선의 구간은 구했지만 그 이후로 거리계산하는 것에서 막힘
# 또한 수식이 너무 더럽다, 내일 다시 짜는걸로,

from sys import stdin
from collections import deque

def circulation(last, cur, check, stack, node):
    global status
    global start_index, end_index, stack_list

    for i in node[cur]:
        if status == 1:
            return False
        if check[i] == False:
            stack.append(i)
            check[i] = True
            circulation(cur, i, check, stack, node)

        elif i != last:
            if last in stack:
                status = 1
                start_index, end_index,stack_list = stack.index(i), stack.index(cur), stack[:]
                return True

    if len(stack):
        cur = stack.pop()
        circulation(cur, i, check, stack, node)

N = int(stdin.readline().strip())
node = [[] for _ in range(N+1)]
check = [False] * (N+1)

for i in range(N):
    A, B = map(int, stdin.readline().split())
    node[A].append(B)
    node[B].append(A)

for i in range(1, N+1):
    node[i].sort()

cir = [1]
check[1] = True
status = 0

start_index = 0
end_index = 0
stack_list = []

circulation(0, 1, check, cir, node)
print(start_index, end_index, stack_list)

Que = deque()
check = [True] * (N+1)
for i in range(start_index, end_index+1):
    check[stack_list[i]] = 0

Que.append(stack_list[start_index])
Que.append(stack_list[end_index])

while Que:
    cur = Que.popleft()
    for i in node[cur]:
        min_ = 3000
        if check[i] == True:
            for o in node[i]:
                if check[o] != True:
                    min_ = min(min_, check[o])
            check[i] = min_ + 1
            Que.append(i)

for i in range(1, N+1):
    print(check[i], end = ' ')