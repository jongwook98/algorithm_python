from sys import stdin
from collections import deque

# 숨바꼭질 3 을 처음 풀 때 -> position[cur] 의 값이 이미 False가 아닌 값으로 채워져 있지만..
# 가중치가 0 인 순간이동이 있으므로 이동하는데 소요되는 시간은 더 짧을 수 있음
# -> 계속 비교하여 최소값을 넣는 방법

N, K = map(int, stdin.readline().split())
position = [False] * (100001)

position[N] = 1

Que = deque()
Que.append(N)

while position[K] == False or len(Que):
    cur_s = Que.popleft()
    if position[K]:
        if position[cur_s] > position[K]:
            continue

    if cur_s < K:
        if position[cur_s+1] == False or (position[cur_s+1] > position[cur_s] + 1):
            position[cur_s+1] = position[cur_s] + 1
            Que.append(cur_s+1)

    if cur_s > 0:
        if position[cur_s-1] == False or (position[cur_s-1] > position[cur_s] + 1):
            position[cur_s-1] = position[cur_s] + 1
            Que.append(cur_s-1)

    if (cur_s*2) <= 100000:
        if position[cur_s*2] == False or (position[cur_s*2] > position[cur_s]):
            position[cur_s*2] = position[cur_s]
            Que.append(cur_s*2)

print(position[K] - 1)