from sys import stdin

def bfs(N, M, move_able):
    check = [[False] * M for _ in range(N)]
    weight_value = [[0] * M for _ in range(N)]
    weight_value[0][0] = 1

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    Que_y = [0]
    Que_x = [0]
    check[0][0] = True

    while len(Que_y):
        if Que_y[0] == N-1 and Que_x[0] == M-1:
            return print(weight_value[N-1][M-1])

        for i in range(len(dx)):
            ny = Que_y[0] + dy[i]
            nx = Que_x[0] + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if check[ny][nx] == False:
                    if move_able[ny][nx]:
                        Que_y.append(ny)
                        Que_x.append(nx)
                        weight_value[ny][nx] = weight_value[Que_y[0]][Que_x[0]] + 1
                        check[ny][nx] = True

        Que_y.pop(0)
        Que_x.pop(0)

N, M = map(int, stdin.readline().split())
move_able = [[] for _ in range(N)]

for i in range(N):
    move_able[i] = list(map(int, stdin.readline().strip()))

bfs(N, M, move_able)