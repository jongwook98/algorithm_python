# check에서 시작 정점으로 부터의 거리를 만들어서
# 목표의 거리들이 오름차순인지 확인하면 될 듯 하다.
# -> 이렇게 계산해버리면 같은 무게값의 다른 부모 노드로부터 파생된 자식 노드를 확인할 수 없다 -> 해결

from sys import stdin
from collections import deque

N = int(stdin.readline().strip())
node = [[] for _ in range(N+1)]
check = [False] * (N+1)

for i in range(N-1):
    A, B = map(int, stdin.readline().split())
    node[A].append(B)
    node[B].append(A)

goal = list(map(int, stdin.readline().split()))

check[1] = [1, 0]
Que = deque()
Que.append(1)

while Que:
    cur = Que.popleft()
    for nd in node[cur]:
        if check[nd] == False:
            Que.append(nd)
            check[nd] = [check[cur][0]+1, cur]

value = check[1][0]
status = 1
parent = 0
parent_check = [False] * (N+1)
Que.append(1)

for i in goal:
    Que.append(i)
    while parent != check[i][1]:
        parent_check[parent] = True
        if len(Que) == 0:
            status = 0
            break
        parent = Que.popleft()

    if status == 0:
        break

    if parent_check[parent] == True:
        status = 0
        break

    if value <= check[i][0]:
        value = check[i][0]
    else:
        status = 0
        break

print(status)