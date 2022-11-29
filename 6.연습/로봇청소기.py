from sys import stdin

N, M = map(int, stdin.readline().split())
Robot = list(map(int, stdin.readline().split()))
Map_arr = [list(map(int, stdin.readline().split())) for _ in range(N)]

check = [[False for _ in range(M)] for _ in range(N) ]
count = 0
rotate_count = 0

dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]

by = [1, 0, -1, 0]
bx = [0, -1, 0, 1]

while True:
    y, x, d = Robot[0], Robot[1], Robot[2]

    if check[y][x] is False and Map_arr[y][x] == 0:
        check[y][x] = True
        count += 1
        rotate_count = 0

    else:
        ny = y + dy[d]
        nx = x + dx[d]
        Robot[2] = (d + 3) % 4
        rotate_count += 1
        if 0 <= ny < N and 0 <= nx < M:
            if check[ny][nx] is False and Map_arr[ny][nx] == 0:
                Robot[0], Robot[1] = ny, nx

            elif rotate_count >= 4:
                if Map_arr[y+by[Robot[2]]][x+bx[Robot[2]]] == 1:
                    break
                else:
                    Robot[0], Robot[1] = y+by[Robot[2]], x+bx[Robot[2]]
                    rotate_count = 0
print(count)