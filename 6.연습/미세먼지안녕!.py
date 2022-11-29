from sys import stdin
from collections import deque
from copy import deepcopy

R, C, T = map(int, stdin.readline().split())
Map = [list(map(int, stdin.readline().split())) for _ in range(R)]
air_filter = []

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

dust_arr = []

for y in range(R):
    for x in range(C):
        if Map[y][x] == -1:
            air_filter.append(y)
        elif Map[y][x] >= 5:
            dust_arr.append((y, x))

up_arr = [(air_filter[0], i) for i in range(1, C)] + \
         [(i, C-1) for i in range(air_filter[0] - 1, -1, -1)] + \
         [(0, i) for i in range(C-2, 0, -1)] + \
         [(i, 0) for i in range(air_filter[0])]

down_arr = [(air_filter[1], i) for i in range(1, C)] + \
           [(i, C-1) for i in range(air_filter[1] + 1, R)] + \
           [(R-1, i) for i in range(C-2, 0, -1)] + \
           [(i, 0) for i in range(R - 1, air_filter[1], -1)]

dir_up = deque(up_arr)
dir_down = deque(down_arr)

time = 0
while time < T:
    time += 1
    next_Map = deepcopy(Map)

    for dust_y, dust_x in dust_arr:
        count = 0
        move_dust = Map[dust_y][dust_x] // 5
        for i in range(4):
            dust_ny = dust_y + dy[i]
            dust_nx = dust_x + dx[i]
            if 0 <= dust_ny < R and 0 <= dust_nx < C and not (dust_ny in air_filter and dust_nx == 0):
                count += 1
                next_Map[dust_ny][dust_nx] += move_dust
        if count > 0:
            next_Map[dust_y][dust_x] -= count * move_dust

    last = 0
    for up in range(len(dir_up)):
        dir_y, dir_x = dir_up[up]
        temp = last
        last = next_Map[dir_y][dir_x]
        next_Map[dir_y][dir_x] = temp

    last = 0
    for down in range(len(dir_down)):
        dir_y, dir_x = dir_down[down]
        temp = last
        last = next_Map[dir_y][dir_x]
        next_Map[dir_y][dir_x] = temp

    Map = deepcopy(next_Map)
    dust_arr = []
    for y in range(R):
        for x in range(C):
            if Map[y][x] >= 5:
                dust_arr.append((y, x))

total_dust = 0
for y in range(R):
    total_dust += sum(Map[y])

print(total_dust + 2)