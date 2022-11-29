# 순환선을 판단하는 기준은 check로 부터 다시 돌아왔을 경우 순환선으로 인식-> DFS 이용하는게 좋을듯?
# stack에 값을 저장해 놓은다음에 순환선을 발견한 그 구간부터 저장된 모든 구간 -> 순환선
# 갈 경로가 사라지면 stack에서 다시 pop 되니까!
# 순환선으로부터 거리는 BFS로 작성 -> 가중치가 모두 1이니까


# 백준 코드 재귀함수에서 return 값을 재귀함수 내의 res 값을 할당하는데 사용했음.
# 함수를 선언하기 전에 만들어두었던 check 리스트를 사용해서 순환선을 구함

import sys

sys.setrecursionlimit(1000000)
from collections import deque

n = int(input())
a = [[] for _ in range(n)]
for _ in range(n):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    a[u].append(v)
    a[v].append(u)

check = [0] * n  # 0: not visited, 1: visited, 2: cycle


def go(x, p):
    # -2: found cycle and not included
    # -1: not found cycle
    # 0~n-1: found cycle and start index

    if check[x] == 1:
        return x

    check[x] = 1
    for y in a[x]:
        if y == p:
            continue
        res = go(y, x)
        if res == -2:
            return -2
        if res >= 0:
            check[x] = 2
            if x == res:
                return -2
            else:
                return res
    return -1


go(0, -1)

q = deque()
dist = [-1] * n

for i in range(n):
    if check[i] == 2:
        dist[i] = 0
        q.append(i)
    else:
        dist[i] = -1

while q:
    x = q.popleft()
    for y in a[x]:
        if dist[y] == -1:
            q.append(y)
            dist[y] = dist[x] + 1

print(*dist, sep=' ')

'''# 시간초과 코드
from sys import stdin
from collections import deque

N = int(stdin.readline().strip())
node = [[] for _ in range(N+1)]
check = [False] * (N+1)

for i in range(N):
    A, B = map(int, stdin.readline().split())
    node[A].append(B)
    node[B].append(A)

print(node)
#for i in range(1, N+1):
#    node[i].sort()

cur = 1
last = 0
check[1] = True
status = 1
stack = [1]

start_index = False
end_index = False
stack_list = []

while status:
    print(stack, cur, last)
    do_pop = 1
    for i in node[cur]:
        if check[i] == False:
            stack.append(i)
            check[i] = True
            last = cur
            cur = i
            do_pop = 0
            break

        elif not i == last:
            if last in stack:
                start_index, end_index, stack_list = stack.index(i), stack.index(cur), stack[:]
                status = 0
                break

    if do_pop and len(stack):
        last = cur
        stack.pop()
        cur = stack[-1]

Que = deque()
check = [True] * (N+1)
for i in range(start_index, end_index+1):
    Que.append(stack_list[i])
    check[stack_list[i]] = 0

while Que:
    cur = Que.popleft()
    for node_ in node[cur]:
        min_ = check[cur]
        if check[node_] == True:
            for o in node[node_]:
                if not check[o] == True:
                    min_ = min(min_, check[o])
            check[node_] = min_ + 1
            Que.append(node_)

for i in range(1, N+1):
    print(check[i], end = ' ')
'''

'''
DFS 로 구현은 성공했지만 정상적인 반환 방법과, 반환이 이뤄진 뒤 이 외의 재귀함수 처리를 어떻게 해야할지 모르겠다.
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
                start_index, end_index, stack_list = stack.index(i), stack.index(cur), stack[:]
                return True

    if len(stack):
        cur_ = stack.pop()
        circulation(cur, cur_, check, stack, node)

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

Que = deque()
check = [True] * (N+1)
for i in range(start_index, end_index+1):
    Que.append(stack_list[i])
    check[stack_list[i]] = 0

while Que:
    cur = Que.popleft()
    for node_ in node[cur]:
        min_ = check[cur]
        if check[node_] == True:
            for o in node[node_]:
                if not check[o] == True:
                    min_ = min(min_, check[o])
            check[node_] = min_ + 1
            Que.append(node_)

for i in range(1, N+1):
    print(check[i], end = ' ')
'''