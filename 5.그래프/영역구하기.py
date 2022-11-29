from sys import stdin
from collections import deque

#세로, 가로
M, N, K = map(int, stdin.readline().split())
rectangle_ = [list(map(int, stdin.readline().split())) for _ in range(K)]

area = [[False for _ in range(N)] for _ in range(M)]
check = [[False for _ in range(N)] for _ in range(M)]

for i in range(K):
    for y in range(rectangle_[i][1], rectangle_[i][3]):
        for x in range(rectangle_[i][0], rectangle_[i][2]):
            area[y][x] = True

Que = deque()
area_arr = []

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

for y in range(M):
    for x in range(N):
        if area[y][x] is False and check[y][x] is False:
            Que.append((y, x))
            check[y][x] = True
            size_ = 0
            while len(Que):
                cur_y, cur_x = Que.popleft()
                size_ += 1
                for i in range(4):
                    ny = cur_y + dy[i]
                    nx = cur_x + dx[i]

                    if 0 <= ny < M and 0 <= nx < N:
                        if check[ny][nx] is False:
                            check[ny][nx] = True
                            if area[ny][nx] is False:
                                Que.append((ny, nx))

            area_arr.append(size_)
# 정렬
area_arr.sort()

print(len(area_arr))
for i in area_arr:
    print(i, end = ' ')