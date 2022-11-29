from sys import stdin
from collections import deque

N = int(stdin.readline())
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]

Que = deque()

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

max_height = 1
for i in range(N):
    max_height = max(max_height, max(arr[i]))

height_arr = [[] for _ in range(max_height + 1)]

for y in range(N):
    for x in range(N):
        height_arr[arr[y][x]].append((y, x))

is_flood = [[False for _ in range(N)] for _ in range(N)]

max_area = 0

for h in range(max_height):
    check = [[False for _ in range(N)] for _ in range(N)]
    area = 0

    for f_y, f_x in height_arr[h]:
        is_flood[f_y][f_x] = True

    for y in range(N):
        for x in range(N):

            if is_flood[y][x] is False and check[y][x] is False:
                area = area + 1
                Que.append((y, x))
                check[y][x] = True

                while len(Que):
                    cur_y, cur_x = Que.popleft()
                    for i in range(4):
                        ny = dy[i] + cur_y
                        nx = dx[i] + cur_x

                        if 0 <= ny < N and 0 <= nx < N:
                            if is_flood[ny][nx] is False and check[ny][nx] is False:
                                Que.append((ny, nx))
                                check[ny][nx] = True

                max_area = max(max_area, area)

print(max_area)