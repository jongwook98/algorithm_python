from sys import stdin
from collections import deque

N, Q = map(int, stdin.readline().split())

Map = [list(map(int, stdin.readline().split())) for _ in range(2 ** N)]
spell = list(map(int, stdin.readline().split()))

move_ = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def rotate(size):
    global Map
    square = 2 ** size
    new_square = [[0 for _ in range(square)] for _ in range(square)]

    if square > 1:
        for i in range(0, 2 ** N, square):
            for j in range(0, 2 ** N, square):
                for t_y in range(square):
                    for t_x in range(square):
                        new_square[t_x][square -1 - t_y] = Map[i + t_y][j + t_x]

                for t_y in range(square):
                    for t_x in range(square):
                        Map[i + t_y][j + t_x] = new_square[t_y][t_x]

    # debug
    #for i in range(2 ** N):
    #    print(Map[i])
    melting()

def melting():
    global Map

    contact = [[4 for _ in range(2 ** N)] for _ in range(2 ** N)]
    for y in range(2 ** N):
        for x in range(2 ** N):
            if y == 0 or y == 2 ** N -1:
                contact[y][x] -= 1
            if x == 0 or x == 2 ** N - 1:
                contact[y][x] -= 1

    for y in range(2 ** N):
        for x in range(2 ** N):
            if Map[y][x] == 0:
                for i in range(4):
                    ny, nx = y + move_[i][0], x + move_[i][1]
                    if 0 <= ny < 2 ** N and 0 <= nx < 2 ** N:
                        contact[ny][nx] -= 1

    for y in range(2 ** N):
        for x in range(2 ** N):
            if contact[y][x] <= 2 and Map[y][x] > 0:
                Map[y][x] -= 1

for i in spell:
    rotate(i)

output = 0
area = 0
Que = deque()

for y in range(2 ** N):
    for x in range(2 ** N):
        output += Map[y][x]

check = [[False for _ in range(2 ** N)] for _ in range(2 ** N)]

for y in range(2 ** N):
    for x in range(2 ** N):
        if check[y][x] is False and Map[y][x] != 0:
            count = 0
            check[y][x] = True
            Que.append([y, x])

            while Que:
                cur_y, cur_x = Que.popleft()
                count += 1
                for i in range(4):
                    ny, nx = cur_y + move_[i][0], cur_x + move_[i][1]
                    if 0 <= ny < 2 ** N and 0 <= nx < 2 ** N:
                        if Map[ny][nx] > 0 and check[ny][nx] is False:
                            Que.append([ny, nx])
                            check[ny][nx] = True

            area = max(count, area)

print(output)
print(area)