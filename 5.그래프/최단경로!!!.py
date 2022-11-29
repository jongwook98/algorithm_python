from sys import stdin
from collections import deque

# 해당 문제는 heapq 구조를 사용해야 시간 초과 에러가 뜨지 않는다고 한다.
# 위 문제는 가중치가 1이 아니기 때문에 일반적인 BFS, deque 구조를 사용하기는 어려운 것 같다.

V, E = map(int, stdin.readline().split())
node = [[] for _ in range(V+1)]
check = [False for _ in range(V+1)]


Head = int(stdin.readline())
for _ in range(E):
    u, v, w = map(int, stdin.readline().split())
    node[u].append([v, w])

Que = deque()
Que.append(Head)
check[Head] = 0

while len(Que):
    cur_ = Que.popleft()
    for i, j in node[cur_]:
        if check[i] == False and i != Head:
            Que.append(i)
            check[i] = check[cur_] + j
        else:
            if check[i] > check[cur_] + j:
                Que.appendleft(i)
                check[i] = check[cur_] + j

for i in range(1, V+1):
    if check[i] != False or i == Head:
        print(check[i])
    else:
        print("INF")