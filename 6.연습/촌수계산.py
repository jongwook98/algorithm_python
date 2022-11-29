from collections import deque

N = int(input())
node = [[] for _ in range(N+1)]
check = [False for _ in range(N+1)]

A, B = map(int, input().split())
M = int(input())

for i in range(M):
    x, y = map(int, input().split())
    node[x].append(y)
    node[y].append(x)

Que = deque([A])
check[A] = 0

while len(Que):
    cur = Que.popleft()
    for i in node[cur]:
        if check[i] is False:
            Que.append(i)
            check[i] = check[cur] + 1

if check[B] is False:
    print(-1)
else:
    print(check[B])