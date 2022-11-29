from sys import stdin
from collections import deque
from copy import deepcopy

# 구현방식을 바꿔야 함
# 배열을 만들어서 쌓여있는 것을 실제로 구현하는 것 -> 단방향 트리?? 구조로 시간을 확 줄여야 함

N, K = map(int, stdin.readline().split())
Map = [list(map(int, stdin.readline().split())) for _ in range(N)]
Map_on = [[0 for _ in range(N)] for _ in range(N)]

piece = []
piece_on = list(deque([i]) for i in range(K))

mv = [[0, 1], [0, -1], [-1, 0], [1, 0]]

for index in range(K):
    r, c, dir_ = map(int, stdin.readline().split())
    piece.append([r-1, c-1, dir_ - 1])
    Map_on[r-1][c-1] = index

stop_flag = False
count = 0

def white_p(num, ny, nx, ndir_):
    global piece, piece_on, Map_on
    piece[num][2] = ndir_
    for index in piece_on[num]:
        piece[index][0], piece[index][1] = ny, nx
    if Map_on[ny][nx] != 0:
        arr = deepcopy(piece_on[Map_on[ny][nx] - 1])
        for cnt, on_ in enumerate(arr):
            arr2 = deepcopy(piece_on[num])
            for index in arr2:
                piece_on[on_].append(index)
            if cnt == 0:
                if len(piece_on[on_]) >= 4:
                    return True
    else:
        Map_on[ny][nx] = num

def red_p(num, ny, nx, ndir_):
    global piece, piece_on, Map_on
    piece[num][2] = ndir_
    swap = deque()
    for index in piece_on[num]:
        piece[index][0], piece[index][1] = ny, nx
    if Map_on[ny][nx] != 0:
        for index in piece_on[num]:
            swap.appendleft(index)
        arr = deepcopy(piece_on[Map_on[ny][nx] - 1])
        for cnt, on_ in enumerate(arr):
            for index in swap:
                piece_on[on_].append(index)
            if cnt == 0:
                if len(piece_on[on_]) >= 4:
                    return True

    else:
        Map_on[ny][nx] = num


def blue_p(num, y, x, ndir_):
    global piece, piece_on, Map_on
    ny, nx = y + mv[ndir_][0], x + mv[ndir_][1]
    if 0 <= ny < N and 0 <= nx < N:
        if Map[ny][nx] == 2:
            ny, nx = y, x
        else:
            Map_on[y][x] = 0
            Map_on[ny][nx] = num
    else:
        ny, nx = y, x

    piece[num][0], piece[num][1], piece[num][2] = ny, nx, ndir_

def move_():
    global count, piece, piece_on, Map_on
    for num, info_ in enumerate(piece):
        y, x, dir_ = info_
        ny, nx = y + mv[dir_][0], x + mv[dir_][1]
        ndir_ = dir_
        if not (0 <= ny < N and 0 <= nx < N):
            if dir_ % 2 == 0:
                ny, nx = y + mv[dir_ + 1][0], x + mv[dir_ + 1][1]
                ndir_ = dir_ + 1
            else:
                ny, nx = y + mv[dir_ - 1][0], x + mv[dir_ - 1][1]
                ndir_ = dir_ - 1

        if Map[ny][nx] == 0:
            Map_on[y][x] = 0
            white_p(num, ny, nx, ndir_)
        elif Map[ny][nx] == 1:
            Map_on[y][x] = 0
            red_p(num, ny, nx, ndir_)
        elif Map[ny][nx] == 2:
            if ndir_ % 2 == 0:
                ndir_ = ndir_ + 1
            else:
                ndir_ = ndir_ - 1
            blue_p(num, y, x, ndir_)

    count += 1

if __name__=="__main__":
    while stop_flag is False and count <= 1000:
        move_()
        print(count)
