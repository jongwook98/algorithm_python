from sys import stdin
from collections import defaultdict

# 제출하자마자 틀리는 에러.

R, C, M = map(int, stdin.readline().split())
input_shark = [list(map(int, stdin.readline().split())) for _ in range(M)]
shark = defaultdict(list)

catch_sum = 0

dy = [1, -1]
dx = [-1, 1]

for r, c, s, d, z in input_shark:
    shark[r - 1, c - 1].append([s, d, z])

def fishing(pos):
    global catch_sum
    global shark

    for y in range(R):
        if (y, pos) in shark.keys():
            info = shark[(y, pos)]
            del shark[(y, pos)]
            catch_sum += info[0][2]

            break

    move_shark()

def move_shark():
    global shark
    new_shark = defaultdict(list)
    for pos, info in shark.items():
        cur_y, cur_x = pos
        for s, d, z in info:
            if d == 1 or d == 2:
                move_ = s % ((R - 1) * 2)
                for _ in range(move_):
                    cur_y += dy[d % 2]
                    if 0 > cur_y or cur_y > (R-1):
                        if d == 1:
                            d = 2
                        else:
                            d = 1

                        cur_y += (dy[d % 2] * 2 )

            else:
                move_ = s % ((C - 1) * 2)
                for _ in range(move_):
                    cur_x += dx[d % 2]
                    if 0 > cur_x or cur_x > (C-1):
                        if d == 3:
                            d = 4
                        else:
                            d = 3

                        cur_x += (dx[d % 2] * 2)

            new_shark[cur_y, cur_x].append([s, d, z])
    shark = new_shark.copy()

    for pos, info in shark.items():
        max_index = -1
        max_value = -1
        if len(info) > 1:
            for n in range(len(info)):
                if info[n][2] > max_value:
                    max_index, max_value = n, info[n][2]

            del new_shark[pos]
            new_shark[pos].append(info[max_index])

    shark = new_shark.copy()
    return True

if __name__=="__main__":
    for x in range(C):
        fishing(x)

    print(catch_sum)