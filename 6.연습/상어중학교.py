# 크기 가장 큰 블록 제거, 점수 획득
# 격자 중력 작용
# 90도 회전
# 중력 작용

# 디버깅이 어려웠던 문제,,
# 문제 분류에 DFS도 포함되어 있었는데 쓰진 않은것 같다.

from sys import stdin
from collections import deque
from copy import deepcopy

N, M = map(int, stdin.readline().split())
Map = [list(map(int, stdin.readline().split())) for _ in range(N)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

total_score = 0

def find_max_size_group():
    global Map

    block_num = [[] for _ in range(M)]
    check = [[[False for _ in range(N)] for _ in range(N)] for _ in range(M)]
    max_count = 0

    for y in range(N):
        for x in range(N):
            if Map[y][x] > 0:
                connection = []
                color = Map[y][x]
                count = 0
                rainbow = 0
                if check[color - 1][y][x] is False:
                    check[color - 1][y][x] = True
                    base_block = [y, x]
                    Que = deque()
                    Que.append((y, x))
                    while len(Que):
                        count += 1
                        cur_y, cur_x = Que.popleft()
                        connection.append([cur_y, cur_x])
                        if Map[cur_y][cur_x] == 0:
                            rainbow += 1
                        for i in range(4):
                            ny = cur_y + dy[i]
                            nx = cur_x + dx[i]
                            if 0 <= ny < N and 0 <= nx < N:
                                if check[color - 1][ny][nx] is False and (Map[ny][nx] == color or (Map[ny][nx] == 0 and Map[ny][nx] is not False)):
                                    check[color - 1][ny][nx] = True
                                    Que.append((ny, nx))
                    block_num[color - 1].append([count, rainbow, base_block, connection])
                    max_count = max(max_count, count)

    if max_count <= 1:
        return True
    flag = 0
    for i in range(M):
        remove_block = []
        for block in block_num[i]:
            if block[0] != max_count:
                remove_block.append(block)
        for block in remove_block:
            block_num[i].remove(block)
        flag += len(block_num[i])

    new_block_arr = []
    max_rainbow = 0
    for i in range(M):
        for block in block_num[i]:
            max_rainbow = max(max_rainbow, block[1])
            new_block_arr.append(block)

    if flag == 1:
        add_score(new_block_arr)
    else:
        flag = 0
        for i in range(M):
            remove_block = []
            for block in block_num[i]:
                if block[1] != max_rainbow:
                    remove_block.append(block)

            for block in remove_block:
                block_num[i].remove(block)
            flag += len(block_num[i])

        new_block_arr = []
        max_row = 0
        for i in range(M):
            for block in block_num[i]:
                max_row = max(max_row, block[2][0])
                new_block_arr.append(block)

        if flag == 1:
            add_score(new_block_arr)
        else:
            flag = 0
            for i in range(M):
                remove_block = []
                for block in block_num[i]:
                    if block[2][0] != max_row:
                        remove_block.append(block)
                for block in remove_block:
                    block_num[i].remove(block)
                flag += len(block_num[i])

            new_block_arr = []
            max_column = 0
            for i in range(M):
                for block in block_num[i]:
                    max_column = max(max_column, block[2][1])
                    new_block_arr.append(block)

            if flag == 1:
                add_score(new_block_arr)
            else:
                new_block_arr = []
                for i in range(M):
                    for block in block_num[i]:
                        if block[2][1] == max_column:
                            new_block_arr.append(block)

                add_score(new_block_arr)

def add_score(block_num):
    global Map
    global total_score

    total_score += block_num[0][0] ** 2

    for cur_y, cur_x in block_num[0][3]:
        Map[cur_y][cur_x] = False
    gravity(0)

def gravity(count):
    global Map

    for x in range(N):
        base_ = N
        for y in range(N-1, -1, -1):
            if Map[y][x] == -1:
                base_ = y
            elif Map[y][x] is not False:
                Map[base_ - 1][x], Map[y][x] = Map[y][x], Map[base_ - 1][x]
                base_ -= 1

    if count == 0:
        rotation()
    elif count == 1:
        find_max_size_group()

def rotation():
    global Map

    new_Map = [[0 for _ in range(N)] for _ in range(N)]
    for y in range(N):
        for x in range(N):
            new_Map[N-1-x][y] = Map[y][x]

    Map = deepcopy(new_Map)

    gravity(1)

if __name__=="__main__":
    find_max_size_group()
    print(total_score)