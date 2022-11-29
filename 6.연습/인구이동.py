from sys import stdin
from collections import deque

N, L, R = map(int, stdin.readline().split())
country = [list(map(int, stdin.readline().split())) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

day_ = 0

# 1 2 4 8 상 우 하 좌

while True:
    fin = False
    Que = deque()
    shared = deque()
    is_open = [[0 for _ in range(N)] for _ in range(N)]

    for y in range(N):
        for x in range(N):
            if y+1 < N:
                if L <= abs(country[y][x] - country[y+1][x]) <= R:
                    fin = True
                    is_open[y][x] += 4
                    is_open[y+1][x] += 1

            if x+1 < N:
                if L <= abs(country[y][x] - country[y][x+1]) <= R:
                    fin = True
                    is_open[y][x] += 2
                    is_open[y][x+1] += 8

    if fin is False:
        break

    day_ += 1
    check = [[False for _ in range(N)] for _ in range(N)]
    # 국경을 개봉하고 나서 이동!
    for y in range(N):
        for x in range(N):
            if is_open[y][x] != 0 and check[y][x] is False:

                Que.clear()
                shared.clear()

                population = country[y][x]
                Que.append((y, x))
                shared.append((y, x))
                check[y][x] = True

                while len(Que):
                    cur_y, cur_x = Que.popleft()
                    check[cur_y][cur_x] = True
                    for i in range(4):
                        ny = cur_y + dy[i]
                        nx = cur_x + dx[i]
                        if 0 <= ny < N and 0 <= nx < N:
                            if check[ny][nx] is False and is_open[cur_y][cur_x] & (2 ** i):
                                check[ny][nx] = True
                                Que.append((ny, nx))
                                shared.append((ny, nx))
                                population += country[ny][nx]

                population //= len(shared)
                for i in shared:
                    country[i[0]][i[1]] = population

print(day_)