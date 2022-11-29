from sys import stdin
from collections import deque

# BFS 이지만 가중치가 0 인 구간을 이동할 때 appendleft를 이용하여 먼저 Que에 들어가도록 하여 -> 최단 거리가 입력되도록 할 수 있다

M, N = map(int, stdin.readline().split())
wall_arr = [[] for _ in range(N)]
check = [[False] * M for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(N):
    wall_arr[i] = list(map(int, stdin.readline().strip()))

Que = deque()
Que.append((0, 0))
check[0][0] = 1

while check[N-1][M-1] == False:
    cur_y, cur_x = Que.popleft()
    for i in range(4):
        ny = cur_y + dy[i]
        nx = cur_x + dx[i]
        if 0 <= ny < N and 0 <= nx < M:
            if check[ny][nx] == False:
                check[ny][nx] = check[cur_y][cur_x] + wall_arr[ny][nx]
                if wall_arr[ny][nx] == 0:
                    Que.appendleft((ny, nx))
                else:
                    Que.append((ny, nx))

print(check[N-1][M-1] - 1)