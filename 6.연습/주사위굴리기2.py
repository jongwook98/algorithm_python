from sys import stdin
from collections import deque

# 2시간 걸렸는데 집중 안한시간 빼면 1시간 40분??

N, M, K = map(int, stdin.readline().split())
Map = [list(map(int, stdin.readline().split())) for _ in range(N)]

dice = [deque((4, 1, 3, 6)), deque((2, 1, 5, 6))]  # [1][0] 서 [2][0] 북 [][1] 윗수 [1][2] 동 [2][2] 남 [][3] -> 아랫수
move_ = [(0, 1), (1, 0), (0, -1), (-1, 0)]

d_y, d_x = 0, 0
dir_ = 0
Sum_ = 0


def move_dice():  # dir 0 ~ 3 -> 동, 남, 서, 북
    global dice, d_y, d_x

    if dir_ // 2 == 1:
        dice[dir_ % 2].append(dice[dir_ % 2].popleft())

    else:
        dice[dir_ % 2].appendleft(dice[dir_ % 2].pop())

    list1, list2 = [], []

    for _ in range(4):
        list1.append(dice[1 - dir_ % 2].popleft())
        list2.append(dice[dir_ % 2].popleft())

    list1[1], list1[3] = list2[1], list2[3]

    for index in range(4):
        dice[1 - dir_ % 2].append(list1[index])
        dice[dir_ % 2].append(list2[index])

    d_y, d_x = d_y + move_[dir_][0], d_x + move_[dir_][1]
    add_score()


def add_score():
    global Sum_, dir_

    check = [[False for _ in range(M)] for _ in range(N)]
    que = deque()
    que.append([d_y, d_x])
    check[d_y][d_x] = True

    base = Map[d_y][d_x]
    count = 1
    while len(que):
        cur_y, cur_x = que.popleft()
        for i in range(4):
            ny, nx = cur_y + move_[i][0], cur_x + move_[i][1]
            if 0 <= ny < N and 0 <= nx < M:
                if check[ny][nx] is False and Map[ny][nx] == Map[cur_y][cur_x]:
                    check[ny][nx] = True
                    que.append([ny, nx])
                    count += 1

    Sum_ += base * count
    dice_ = dice[0].pop()
    dice[0].append(dice_)

    if dice_ > Map[d_y][d_x]:
        dir_ = (dir_ + 1) % 4
    elif dice_ < Map[d_y][d_x]:
        dir_ = (dir_ + 3) % 4

    ny, nx = d_y + move_[dir_][0], d_x + move_[dir_][1]
    if not (0 <= ny < N and 0 <= nx < M):
        dir_ = (dir_ + 2) % 4


if __name__=="__main__":
    for _ in range(K):
        move_dice()

    print(Sum_)
