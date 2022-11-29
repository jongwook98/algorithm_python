from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
position = [False] * (100001)
position[N] = 1

Que = deque()
Que.append(N)

while position[M] == False:
    cur_s = Que.popleft()
    if (cur_s) < M:
        if position[cur_s + 1] == False:
            position[cur_s + 1] = position[cur_s] + 1
            Que.append(cur_s + 1)

    if (cur_s) > 0:
        if position[cur_s - 1] == False:
            position[cur_s - 1] = position[cur_s] + 1
            Que.append(cur_s - 1)

    if (cur_s) < M and (cur_s*2) <= 100000:
        if position[cur_s*2] == False:
            position[cur_s*2] = position[cur_s] + 1
            Que.append(cur_s*2)

print(position[M]-1)