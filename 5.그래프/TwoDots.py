# DFS로 풀되, 초기 시작점을 저장, 다시 돌아올 수 있다면 사이클로 인정 BFS는 어려워 보인다...
# 함수 매개변수가 너무 많긴한데,, 맞았다. 다음엔 좀 깔끔하게 하는 방법으로 해보자.
from sys import stdin

def move(check, sign, dot_arr, cur_y, cur_x, ly, lx, dy, dx):
    global cycle

    for o in range(len(dy)):
        ny = cur_y + dy[o]
        nx = cur_x + dx[o]
        if 0 <= ny < N and 0 <= nx < M:
            if ny == ly and nx == lx:
                pass
            else:
                if dot_arr[ny][nx] == sign:
                    if check[ny][nx] == False:
                        check[ny][nx] = True
                        move(check, sign, dot_arr, ny, nx, cur_y, cur_x, dy, dx)
                    else:
                        cycle = "Yes"
                        return

N, M = map(int, stdin.readline().split())
dot_arr = [[] for _ in range(N)]
check = [[False] * M for _ in range(N)]

cycle = "No"

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for i in range(N):
    dot_arr[i] = list(stdin.readline().strip())

for Y in range(N):
    for X in range(M):
        if check[Y][X] == False:
            check[Y][X] = True
            move(check, dot_arr[Y][X], dot_arr, Y, X, 0, 0, dy, dx)

print(cycle)