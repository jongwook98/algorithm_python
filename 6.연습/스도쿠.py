# 구글링해서 얻은 코드

import sys
graph = []
blank = []

for i in range(9):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i, j))

def checkRow(x, a):
    for i in range(9):
        if a == graph[x][i]:
            return False
    return True

def checkCol(y, a):
    for i in range(9):
        if a == graph[i][y]:
            return False
    return True

def checkRect(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == graph[nx+i][ny+j]:
                return False
    return True


def dfs(idx):
    if idx == len(blank):
        for i in range(9):
            print(*graph[i]) # -> 새로 배운것 list unpacking을 한단다
        exit(0)              # -> 코드 종료해버리기 -> 사용하기 괜찮은 것 같다

    for i in range(1, 10):
        x = blank[idx][0]
        y = blank[idx][1]

        if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i):
            graph[x][y] = i
            dfs(idx+1)
            graph[x][y] = 0

dfs(0)

# 내가 시도했던 코드로 -> 너무 어렵게 접근했다.

#   내 풀이 과정
# 1. 주어진 초기 스도쿠 조건에서 중복되는 것을 배제하고 생각하기 위해 미리 제거하고 시작
# 2. 각각의 빈칸에 대해서 열, 줄, 사각형의 조건을 고려하여 답이 정해져 있는 부분은 넣고 다시 배제하고 시작
# 3. 그러다가 답이 정해져 있는 부분이 없다면 DFS + 백트래킹으로 찾기!

# 최대한 시간을 줄이기 위해서 시도 했던 것이
# 고려할 것이 많아지면서 ( 이미 값이 들어가 있는 부분, 값을 넣어준 부분 )
# 열, 줄, 사각형의 조건을 다시 비교하기가 어려웠다.

'''
from sys import stdin
from copy import deepcopy

Map = [list(map(int, stdin.readline().split())) for _ in range(9)]

candi_row = [[i for i in range(1, 10)] for _ in range(9)]
candi_col = [[i for i in range(1, 10)] for _ in range(9)]
candi_sq = [[[i for i in range(1, 10)] for _ in range(3)] for _ in range(3)]
solve = []

for y in range(9):
    for x in range(9):
        if Map[y][x] == 0:
            solve.append([y, x])
        else:
            candi_row[y].remove(Map[y][x])
            candi_col[x].remove(Map[y][x])
            candi_sq[y // 3][x // 3].remove(Map[y][x])

cnt = len(solve)
solve_candi = [0 for _ in range(len(solve))]


def make_Map(arr):
    row, col, sq = deepcopy(candi_row), deepcopy(candi_col), deepcopy(candi_sq)
    for num, index in enumerate(arr):

        for num, info_ in enumerate(solve):
            y, x = info_[0], info_[1]
            candi_ = candi_row[y].copy()
            candi_2 = []
            candi_f = []

            for index in candi_col[x]:
                if index in candi_:
                    candi_2.append(index)
            for index in candi_sq[y // 3][x // 3]:
                if index in candi_2:
                    candi_f.append(index)
            solve_candi[num] = candi_f.copy()

        if index == 0:
            continue
        y, x = solve[num]
        Map[y][x] = index


def DFS(solved, candi, n, index): # n -> 몇 번째 solve 하고 있었는지, index -> candi의 몇 번째 index를 시도하고 있었는지
    global Map, cnt

    if n >= len(solve):
        return make_Map(solved)
    if index > len(candi[n]):
        return False

    y, x = solve[n]
    if Map[y][x] != 0:
        solved.append(0)
        DFS(solved, candi, n + 1, 0)

    else:
        Map[y][x] = candi[n][index]
        solved.append(candi[n][index])
        DFS(solved, candi, n + 1, 0)

        Map[y][x] = 0
        solved.pop()
        DFS(solved, candi, n, index + 1)


def fill_candi():
    global Map, solve_candi, cnt
    while cnt:
        swap_candi = deepcopy(solve_candi)
        flag = True
        for num, arr in enumerate(swap_candi):
            if len(arr) == 1:
                flag = False
                y, x = solve[num]
                Map[y][x] = arr[0]
                cnt -= 1
                if arr[0] in candi_row[y]:
                    candi_row[y].remove(arr[0])
                if arr[0] in candi_col[x]:
                    candi_col[x].remove(arr[0])
                if arr[0] in candi_sq[y // 3][x // 3]:
                    candi_sq[y // 3][x // 3].remove(arr[0])

        # 경우의 수
        if flag is True:
            solved = []
            DFS(solved, swap_candi, 0, 0)


def make_candi():
    global solve_candi
    for num, info_ in enumerate(solve):
        y, x = info_[0], info_[1]
        candi_ = candi_row[y].copy()
        candi_2 = []
        candi_f = []

        for index in candi_col[x]:
            if index in candi_:
                candi_2.append(index)
        for index in candi_sq[y // 3][x // 3]:
            if index in candi_2:
                candi_f.append(index)
        solve_candi[num] = candi_f.copy()


make_candi()
fill_candi()

for y in range(9):
    for x in range(9):
        print(Map[y][x], end=" ")
    print()
'''