from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
check = [[[False for _ in range(2)] for _ in range(M)] for _ in range(N)]
Map = [list(stdin.readline().strip()) for _ in range(N)]

Que = deque([(0, 0, 0)])
check[0][0][0] = 1
check[0][0][1] = 1

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

output = -1

if N == 1 and M == 1:
    output = 1

while len(Que):
    cur_y, cur_x, chance = Que.popleft()
    for i in range(4):
        ny = cur_y + dy[i]
        nx = cur_x + dx[i]
        if 0 <= ny < N and 0 <= nx < M:
            if ny == N-1 and nx == M-1:
                output = check[cur_y][cur_x][chance] + 1
                Que.clear()
                break

            elif Map[ny][nx] == '0' and check[ny][nx][chance] is False:
                Que.append((ny, nx, chance))
                check[ny][nx][chance] = check[cur_y][cur_x][chance] + 1

            elif Map[ny][nx] == '1' and chance == 0:
                Que.append((ny, nx, 1))
                check[ny][nx][1] = check[cur_y][cur_x][chance] + 1

print(output)