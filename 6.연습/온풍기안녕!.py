from sys import stdin
from collections import deque
from copy import deepcopy

# 2022-09-14 문제 푼지 1시간 30분 경과.. 바람이 한 번 나오는게 잘 안됨 -> 방향과 무브 테이블 확인
# 2022-09-14 3:40 머리 자르고 와서 다시 시작 2022-09-14 4:20 끝

R, C, K = map(int, stdin.readline().split())
Map = [list(map(int, stdin.readline().split())) for _ in range(R)]
wall_Map = [[0 for _ in range(C)] for _ in range(R)]

W = int(stdin.readline().strip())
wall_info = [list(map(int, stdin.readline().split())) for _ in range(W)]

move_ = [
    [0, 1],    #0 #1
    [0, -1],   #1 #2
    [-1, 0],   #2 #4
    [1, 0]     #3 #8
]

move_table = [  # 검사 벽, 이동 순서 (확산)
    [[0], [2, 0], [3, 0]],
    [[1], [2, 1], [3, 1]],
    [[2], [0, 2], [1, 2]],
    [[3], [0, 3], [1, 3]]
]

# 1 2 4 8 동 서 북 남
for wall in wall_info:
    y, x = wall[0] - 1, wall[1] - 1
    if wall[2] == 1:
        wall_Map[y][x] |= 1
        wall_Map[y][x + 1] |= 2
    elif wall[2] == 0:
        wall_Map[y][x] |= 4
        wall_Map[y - 1][x] |= 8

chocolate = 0
system = []
condition = []

stop_flag = False

for y in range(R):
    for x in range(C):
        if Map[y][x] in [1, 2, 3, 4]:
           system.append((y, x, Map[y][x] - 1))
        elif Map[y][x] == 5:
            condition.append((y, x))

Map = [[0 for _ in range(C)] for _ in range(R)]

def wind():  # 벽체크하고, 바람 퍼트리기
    global Map
    for y, x, dir in system:
        check = [[False for _ in range(C)] for _ in range(R)]
        check[y][x] = True
        cy, cx = y + move_[dir][0], x + move_[dir][1]
        if 0 <= cy < R and 0 <= cx < C and not (wall_Map[y][x] & (2 ** dir)):
            check[cy][cx] = True
            cnt = 5
            Map[cy][cx] += cnt
            que = deque()
            que.append([cy, cx])

            while len(que) and cnt:
                cnt -= 1
                rep = len(que)
                for _ in range(rep):
                    con_y, con_x = que.popleft()
                    for num in range(3):
                        cur_y, cur_x = con_y, con_x
                        for seq in move_table[dir][num]:
                            ny, nx = cur_y + move_[seq][0], cur_x + move_[seq][1]
                            if 0 <= ny < R and 0 <= nx < C and not (wall_Map[cur_y][cur_x] & (2 ** seq)):
                                cur_y, cur_x = ny, nx
                                if check[ny][nx] is False and seq == move_table[dir][num][-1]:
                                    check[cur_y][cur_x] = True
                                    Map[cur_y][cur_x] += cnt
                                    que.append([cur_y, cur_x])
    temperate()
        # #debug
        # for i in range(R):
        #     print(Map[i])
        # print()

# wind()
# for i in range(R):
#     print(Map[i])


def temperate():
    global Map
    temp_Map = deepcopy(Map)

    for y in range(R):
        for x in range(C):
            for i in range(4):
                ny, nx = y + move_[i][0], x + move_[i][1]
                if 0 <= ny < R and 0 <= nx < C:
                    temp = (Map[y][x] - Map[ny][nx]) // 4
                    if temp > 0 and not (wall_Map[y][x] & (2 ** i)):
                        temp_Map[y][x] -= temp
                        temp_Map[ny][nx] += temp

    Map = deepcopy(temp_Map)

    decrease()

    # #debug
    # for i in range(R):
    #     print(Map[i])



def decrease():
    global chocolate, Map, stop_flag
    chocolate += 1

    stop_flag = True

    for y in range(R):
        for x in range(C):
            if y == 0 and Map[y][x] > 0:
                Map[y][x] -= 1
            elif y == R-1 and Map[y][x] > 0:
                Map[y][x] -= 1
            elif x == 0 and Map[y][x] > 0:
                Map[y][x] -= 1
            elif x == C-1 and Map[y][x] > 0:
                Map[y][x] -= 1

    for y, x in condition:
        if Map[y][x] < K:
            stop_flag = False
            break

    # #debug
    # for i in range(R):
    #     print(Map[i])

if __name__=="__main__":
    while chocolate <= 100 and not stop_flag:
       wind()
    print(chocolate)