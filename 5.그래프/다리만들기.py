from sys import stdin
from collections import deque

# BFS를 이용하며 섬의 구분 기호, 섬에서의 거리를 측정하여 구분 기호가 다른 두 섬이 만나는 순간이 가장 작은 다리 개수

N = int(stdin.readline().strip())
map_arr = [[] for _ in range(N)]
check = [[False] * N for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

cnt = 1
Que = deque()
island_Que = deque()

for i in range(N):
    map_arr[i] = list(map(int, stdin.readline().split()))

def BFS(Que, sign):
    while len(Que):
        cur_y, cur_x = Que.popleft()
        for i in range(4):
            ny = cur_y + dy[i]
            nx = cur_x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if check[ny][nx] == False:
                    if map_arr[ny][nx] == 1:
                        check[ny][nx] = [0, sign]
                        Que.append((ny, nx))

for i in range(N):
    for j in range(N):
        if map_arr[i][j] == 1:
            if check[i][j] == False:
                Que.append((i, j))
                check[i][j] = [0, cnt]
                BFS(Que, cnt)
                cnt += 1
            island_Que.append((i, j))

status = 1
min_ = 10000

while len(island_Que):
    cur_y, cur_x = island_Que.popleft()
    for i in range(4):
        ny = cur_y + dy[i]
        nx = cur_x + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if check[ny][nx] == False:
                check[ny][nx] = [check[cur_y][cur_x][0] + 1, check[cur_y][cur_x][1]]
                if status:
                    island_Que.append((ny, nx))
            elif check[ny][nx][1] != check[cur_y][cur_x][1]:
                min_ = min(min_, check[ny][nx][0] + check[cur_y][cur_x][0])
                status = 0
                break

print(min_)