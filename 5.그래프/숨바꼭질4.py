from sys import stdin
from collections import deque

N, K = map(int, stdin.readline().split())
position = [False] * (100001)


Que = deque()
Que.append(N)
position[N] = [1, False]

while position[K] == False:
    cur_s = Que.popleft()

    if cur_s < K:
        if position[cur_s + 1] == False:
            position[cur_s + 1] = [position[cur_s][0] + 1, cur_s]
            Que.append(cur_s+1)

    if cur_s > 0:
        if position[cur_s - 1] == False:
            position[cur_s - 1] = [position[cur_s][0] + 1, cur_s]
            Que.append(cur_s - 1)

    if (cur_s*2) <= 100000 and cur_s < K:
        if position[cur_s*2] == False:
            position[cur_s*2] = [position[cur_s][0] + 1, cur_s]
            Que.append(cur_s*2)

print(position[K][0] - 1)
output = [K]
cur = K

for i in range(1, position[K][0]):
    cur = position[cur][1]
    output.append(cur)

for i in range(len(output)-1, -1, -1):
    print(output[i], end=' ')