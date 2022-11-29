from sys import stdin
from collections import deque

N = int(stdin.readline().strip())
node = [[] for _ in range(N+1)]
check = [False] * (N+1)
Que = deque()

for i in range(N-1):
    A, B = map(int, stdin.readline().split())
    node[A].append(B)
    node[B].append(A)

Que.append(1)
while len(Que):
    cur = Que.popleft()
    for i in node[cur]:
        if check[i] == False:
            check[i] = cur
            Que.append(i)

for i in range(2, N+1):
    print(check[i])