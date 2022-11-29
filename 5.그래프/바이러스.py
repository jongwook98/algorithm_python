from sys import stdin
from collections import deque

total = int(stdin.readline())
node = [[] for _ in range(total+1)]
check = [False] * (total+1)

N = int(stdin.readline())

for _ in range(N):
    A, B = map(int, stdin.readline().split())
    node[A].append(B)
    node[B].append(A)

Que = deque()
Que.append(1)
check[1] = True
count = 0

while len(Que):
    cur = Que.popleft()
    for tar in node[cur]:
        if check[tar] == False:
            count = count + 1
            Que.append(tar)
            check[tar] = True

print(count)