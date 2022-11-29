# BFS, 지나간 경로가 맞는지 확인은 +1 로봇의 명령은 +2로 중복안나게 구현

from sys import stdin
from collections import deque

H, W = map(int ,stdin.readline().split())
Map_arr = [list(stdin.readline().strip()) for _ in range(H)]

check = [[False for _ in range(W)] for _ in range(H)]

Que = deque()

sy = [0, 0, 1, -1]
sx = [1, -1, 0, 0]

dy = [0, 0, 2, -2]
dx = [2, -2, 0, 0]

pose_sig = ['>', '<', 'v', '^']
dir_sig = ['', 'R', 'L', 'R', 'L']

start_ = False

for y in range(H):
    for x in range(W):
        if start_ is not False:
            break

        if Map_arr[y][x] == '#':
            Que.append((y, x))
            check[y][x] = True

            while len(Que):
                cur_y, cur_x = Que.popleft()
                flag = 0
                for i in range(4):
                    ny = cur_y + sy[i]
                    nx = cur_x + sx[i]

                    if 0 <= ny < H and 0 <= nx < W:
                        if check[ny][nx] is False and Map_arr[ny][nx] == '#':
                            flag = 1
                            Que.append((ny, nx))
                            check[ny][nx] = True

                if flag == 0:
                    start_ = (cur_y + 1, cur_x + 1)
    if start_ is not False:
        break

check = [[False for _ in range(W)] for _ in range(H)]
Que.append((start_[0] - 1, start_[1] - 1))
check[start_[0] - 1][start_[1] - 1] = True

init_pose = False
order_arr = []

Robot_dir = 0

while len(Que):
    cur_y, cur_x = Que.popleft()
    flag = 0
    for i in range(4):
        ny_2 = cur_y + dy[i]
        nx_2 = cur_x + dx[i]

        ny_1 = cur_y + sy[i]
        nx_1 = cur_x + sx[i]

        if 0 <= ny_2 < H and 0 <= nx_2 < W:
            if check[ny_2][nx_2] is False and Map_arr[ny_1][nx_1] == '#':

                if init_pose is False:
                    init_pose = pose_sig[i]
                else:
                    order_arr.append(dir_sig[Robot_dir - i])

                order_arr.append('A')
                Robot_dir = i
                Que.append((ny_2, nx_2))
                check[ny_2][nx_2] = True

print(start_[0], start_[1])
print(init_pose)

print(''.join(order_arr))