from sys import stdin

M, N = map(int, stdin.readline().split())
tomato = [[] for _ in range(N)]
spread_y = []
spread_x = []
count = 0 # 안익은 토마토 남은 개수
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

for i in range(N):
    tomato[i] = list(map(int, stdin.readline().split()))

for Y in range(N):
    for X in range(M):
        if tomato[Y][X] == 1:
            spread_y.append(Y)
            spread_x.append(X)
        elif tomato[Y][X] == 0:
            count += 1

Que_y = spread_y
Que_x = spread_x

while Que_y:
    cur_y = Que_y[0]
    cur_x = Que_x[0]
    for i in range(4):
        ny = cur_y + dy[i]
        nx = cur_x + dx[i]
        if 0 <= ny < N and 0 <= nx < M:
            if tomato[ny][nx] == 0:
                Que_y.append(ny)
                Que_x.append(nx)
                tomato[ny][nx] = tomato[cur_y][cur_x] + 1
                count -= 1

    Que_y.pop(0)
    Que_x.pop(0)

if count == 0:
    print(tomato[cur_y][cur_x] - 1)
else:
    print(-1)