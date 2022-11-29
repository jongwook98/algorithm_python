from sys import stdin
from collections import deque

def BFS():
    M, N, H = map(int, stdin.readline().split())
    check = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]

    tomato = [[list(map(int, stdin.readline().split())) for _ in range(N)] for _ in range(H)]

    Que = deque()

    dy = [0, 0, 1, -1, 0, 0]
    dx = [1, -1, 0, 0, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    count = 0
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if tomato[h][n][m] == 1:
                    Que.append((h, n, m))
                    check[h][n][m] = 0

                elif tomato[h][n][m] == 0:
                    count += 1

    if count == 0:
        return 0

    while len(Que):
        cur_z, cur_y, cur_x = Que.popleft()
        for i in range(6):
            nz = cur_z + dz[i]
            ny = cur_y + dy[i]
            nx = cur_x + dx[i]
            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
                if check[nz][ny][nx] is False and tomato[nz][ny][nx] == 0:
                    check[nz][ny][nx] = check[cur_z][cur_y][cur_x] + 1
                    count -= 1
                    if count == 0:
                        return check[nz][ny][nx]
                    Que.append((nz, ny, nx))

    return -1

if __name__=="__main__":
    print(BFS())