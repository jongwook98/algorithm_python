from sys import stdin
from collections import deque

N = int(stdin.readline())
paint_arr = [list(stdin.readline().strip()) for _ in range(N)]

check = [[False for _ in range(N)] for _ in range(N)]
check_GR = [[False for _ in range(N)] for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

Que = deque()
Que_GR = deque()

count_ = 0
count_GR = 0

for y in range(N):
    for x in range(N):
        if check[y][x] is False:
            Que.append((y, x))
            count_ = count_ + 1

            while len(Que):
                cur_y, cur_x = Que.popleft()

                for i in range(4):
                    ny = dy[i] + cur_y
                    nx = dx[i] + cur_x

                    if 0 <= ny < N and 0 <= nx < N:
                        if check[ny][nx] is False:
                            if paint_arr[cur_y][cur_x] == paint_arr[ny][nx]:
                                Que.append((ny, nx))
                                check[ny][nx] = True

        if check_GR[y][x] is False:
            Que_GR.append((y, x))
            count_GR = count_GR + 1

            while len(Que_GR):
                cur_y, cur_x = Que_GR.popleft()

                for i in range(4):
                    ny = dy[i] + cur_y
                    nx = dx[i] + cur_x

                    if 0 <= ny < N and 0 <= nx < N:
                        if check_GR[ny][nx] is False:
                            if paint_arr[cur_y][cur_x] == paint_arr[ny][nx] or \
                                    (paint_arr[cur_y][cur_x] in ['G', 'R'] and paint_arr[ny][nx] in ['G', 'R']):
                                Que_GR.append((ny, nx))
                                check_GR[ny][nx] = True

print(count_, count_GR, end=' ')