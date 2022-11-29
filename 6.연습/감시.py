# copy.deepcopy 사용한 이유
# python list를 복사할 때 list 슬라이싱으로 복사하면 깊은 복사가 되는 것으로 알고 있고
# 슬라이싱으로 복사하는 것이 가장 빠르다고 알고 있는데
# 자꾸 얕은 복사가 되는지 이유를 찾아보니 list의 인덱스 중에서
# 오브젝트를 포함하는 경우?? 얕은복사가 된다고 한다. 아마 이중이상의 배열에서 얕은 복사가 되는 듯,,
# 하지만 deepcopy는 이중 이상의 배열의 깊은 복사가 가능하기 때문에 사용한다!

from sys import stdin
from collections import deque
from itertools import product
import copy

N, M = map(int, stdin.readline().split())
Map_arr = [list(map(int, stdin.readline().split())) for _ in range(N)]

count_arr = []

CCTV_ = []
# 방향 1  2  4  8
#     북  동  남  서
CC_1 = deque([1, 0, 0, 0])
CC_2 = deque([1, 0, 1, 0])
CC_3 = deque([1, 1, 0, 0])
CC_4 = deque([1, 1, 1, 0])
CC_5 = deque([1, 1, 1, 1])

CC_DIR = [CC_1, CC_2, CC_3, CC_4, CC_5]

check_base = [[False for _ in range(M)] for _ in range(N)]

for y in range(N):
    for x in range(M):
        if Map_arr[y][x] in [1, 2, 3, 4, 5]:
            CCTV_.append([y, x, (Map_arr[y][x]-1), 0])
            check_base[y][x] = True
        elif Map_arr[y][x] == 6:
            check_base[y][x] = True

CCTV_DIR = [deque() for _ in range(len(CCTV_))]

def is_CHECK(y, x, dir, check, Map_arr):
    if dir[0] == 1:
        b_y, b_x = y, x
        while True:
            b_y -= 1
            if 0 <= b_y < N:
                if Map_arr[b_y][b_x] == 6:
                    break
                check[b_y][b_x] = True
            else:
                break

    if dir[1] == 1:
        b_y, b_x = y, x
        while True:
            b_x += 1
            if 0 <= b_x < M:
                if Map_arr[b_y][b_x] == 6:
                    break
                check[b_y][b_x] = True
            else:
                break
    if dir[2] == 1:
        b_y, b_x = y, x
        while True:
            b_y += 1
            if 0 <= b_y < N:
                if Map_arr[b_y][b_x] == 6:
                    break
                check[b_y][b_x] = True
            else:
                break
    if dir[3] == 1:
        b_y, b_x = y, x
        while True:
            b_x -= 1
            if 0 <= b_x < M:
                if Map_arr[b_y][b_x] == 6:
                    break
                check[b_y][b_x] = True
            else:
                break

    return

# CCTV 들의 방향 정하는 중복순열 함수 product
# 전체 경우를 탐색해서 확인해도 될 듯! 4의 8승 이니까 시간초과는 안날듯 하다
# 시간초과는 안났는데 copy 모듈의 deepcopy 를 이용하다보니까 시간이 오려걸렸다.

# itertools 모듈의 product 함수를 사용해서 중복순열을 만들어서 구현!
for dir in product([0, 1, 2, 3], repeat = len(CCTV_)):
    count = 0
    check = copy.deepcopy(check_base)

    # CCTV 보는 방향 설정
    for i in range(len(CCTV_)):
        CCTV_DIR[i] = CC_DIR[CCTV_[i][2]].copy()

        for r in range(dir[i]):
            CCTV_DIR[i].appendleft(CCTV_DIR[i].pop())

    # CCTV가 감시하는 구간 check 하기
    for i in range(len(CCTV_)):
        cur_y, cur_x = CCTV_[i][0], CCTV_[i][1]
        is_CHECK(cur_y, cur_x, CCTV_DIR[i], check, Map_arr)

    # 감시하지 못하는 영역 개수 세기
    for y in range(N):
        for x in range(M):
            if check[y][x] is False:
                count += 1
    count_arr.append(count)

print(min(count_arr))