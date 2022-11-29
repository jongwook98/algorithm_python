# 구현 문제였고, deque 자료구조를 이용해 앞에서, 뒤에서 자유롭게 인덱스 변경을 쉽게 했다.!

from sys import stdin
from collections import deque

gear_ = [list(map(int, stdin.readline().strip())) for _ in range(4)]
K = int(stdin.readline())

rotate = [list(map(int, stdin.readline().split())) for _ in range(K)]
de_rotate = [deque() for _ in range(4)]

for i in range(4):
    for j in range(8):
        de_rotate[i].append(gear_[i][j])

rotate_state = [0, 0, 0, 0]
contact_gear = [2, 6] # 앞의 기어, 뒤의 기어 접하는 부분

score = 0

for n in range(K):
    is_rotate = [0, 0, 0, 0]
    base_gear, spin_dir = (rotate[n][0]-1), rotate[n][1]

    is_rotate[base_gear] = spin_dir

    for i in range(base_gear):
        if de_rotate[(base_gear - i - 1)][contact_gear[0]] != de_rotate[(base_gear - i)][contact_gear[1]]:
            is_rotate[base_gear - i - 1] = -(is_rotate[base_gear - i])
        else:
            break

    for i in range(len(gear_) - 1 - base_gear):
        if de_rotate[(base_gear + i)][contact_gear[0]] != de_rotate[(base_gear + i + 1)][contact_gear[1]]:
            is_rotate[base_gear + i + 1] = -(is_rotate[base_gear + i])
        else:
            break

    for i in range(4):
        if is_rotate[i] == 1:
            de_rotate[i].appendleft(de_rotate[i].pop())
        elif is_rotate[i] == -1:
            de_rotate[i].append(de_rotate[i].popleft())

for n in range(4):
    score = score + (2 ** n * de_rotate[n][0])

print(score)