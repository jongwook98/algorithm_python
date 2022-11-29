from sys import stdin
from copy import deepcopy

RIGHT = 1
LEFT = 0

# 사다리의 최대 개수가 3개 이므로 브루트포스 알고리즘 이용

N, M, H = map(int, stdin.readline().split())
ladder_arr = [[[False, False] for _ in range(N)] for _ in range(H)]

for _ in range(M):
    row, column = map(int, stdin.readline().split())
    ladder_arr[row - 1][column - 1][RIGHT] = True
    ladder_arr[row - 1][column][LEFT] = True

# 사다리가 겹치지 않도록 만드는 함수
def make_ladder(ladder_arr, pos, count, index):
    if index >= count:
        return ladder_game(ladder_arr, count)

    if pos > N * H:
        return print(-1)

    row = pos // N
    column = pos % N

    print("pos:", pos, "count:", count, "index:", index)
    for i in range(H):
        print(ladder_arr[i])

    if ladder_arr[row][column][RIGHT] or ladder_arr[row][column][LEFT]:
        make_ladder(ladder_arr, pos + 1, count, index)
    elif column - 1 >= 0:
        if ladder_arr[row][column - 1][RIGHT] is False and ladder_arr[row][column - 1][LEFT] is False:
            ladder_arr[row][column - 1][RIGHT] = True
            ladder_arr[row][column][LEFT] = True

            make_ladder(ladder_arr, pos + 1, count, index + 1)

            ladder_arr[row][column - 1][RIGHT] = False
            ladder_arr[row][column][LEFT] = False

            make_ladder(ladder_arr, pos + 1, count, index)

        else:
            make_ladder(ladder_arr, pos + 1, count, index)
    else:
        make_ladder(ladder_arr, pos + 1, count, index)

# 만들어진 사다리로 게임을 했을 때 조건을 만족하는지 판단
def ladder_game(Map, count):
    for i in range(N):
        cur = i
        for h in range(H):
            if Map[h][cur][LEFT] == True:
                cur = i - 1
            elif Map[h][cur][RIGHT] == True:
                cur = i + 1
        if cur != i:
            return print("Fail")
            #return False

    return print(count)

for i in range(4):
    make_ladder(ladder_arr, 0, i, 0)