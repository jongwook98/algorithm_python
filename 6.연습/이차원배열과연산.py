from sys import stdin
from collections import defaultdict

# defaultdict 를 이용한 딕셔너리 구조 공부

# defaultdict(list) - dictionary value 를 list로 받아옴
# defaultdict(int) - dictionaray value 를 int로 받아옴

# dictionary 구조를 sort 할 때
# dict = sorted(dictionary.items(), key = lambda item: (1번 조건식, 2번 조건식) 으로 다중 조건으로 정렬 가능

# 예시 new_ = sorted(new_.items(), key = lambda item: (item[1], item[0]))
# value 크기로 오름차순 정렬 후 key 크기로 오름차순 정렬 가능

# new_ = sorted(new_.items(), key = lambda item: len(item[1]))
# 이런식으로 defaultdict 가 list 라면 value 원소의 개수로 정렬 가능


r, c, k = map(int, stdin.readline().split())
r = r - 1
c = c - 1
Map = [list(map(int, stdin.readline().split())) for _ in range(3)]

row = 3
column = 3

def R_calcul(time):
    global row, column, Map

    new_ = [defaultdict(int) for _ in range(row)]
    max_column = 0
    for y in range(row):
        for x in range(column):
            if Map[y][x] == 0:
                continue
            if Map[y][x] in new_[y].keys():
                new_[y][Map[y][x]] += 1
            else:
                new_[y][Map[y][x]] = 1


    for y in range(row):
        new_[y] = sorted(new_[y].items(), key = lambda item: (item[1], item[0]))
        max_column = max(max_column, len(new_[y]))
    Map = [[0 for _ in range(max_column * 2)] for _ in range(row)]

    for y in range(row):
        for num, value in enumerate(new_[y]):
            Map[y][num * 2], Map[y][num * 2 + 1] = value[0], value[1]

    column = max_column * 2
    if column > 100:
        Map = Map[:][:100]
        column = 100

    if r < row and c < column:
        if Map[r][c] == k:
            return True

    return False


def C_calcul(time):
    global row, column, Map

    new_ = [defaultdict(int) for _ in range(column)]
    max_row = 0
    for x in range(column):
        for y in range(row):
            if Map[y][x] == 0:
                continue
            if Map[y][x] in new_[x].keys():
                new_[x][Map[y][x]] += 1
            else:
                new_[x][Map[y][x]] = 1

    for x in range(column):
        new_[x] = sorted(new_[x].items(), key = lambda item: (item[1], item[0]))
        max_row = max(max_row, len(new_[x]))
    Map = [[0 for _ in range(column)] for _ in range(max_row * 2)]

    for x in range(column):
        for num, value in enumerate(new_[x]):
            Map[num * 2][x], Map[num * 2 + 1][x] = value[0], value[1]

    row = max_row * 2
    if row > 100:
        Map = Map[:100][:]
        row = 100

    if r < row and c < column:
        if Map[r][c] == k:
            return True

    return False

if __name__=="__main__":
    flag = 0
    for time in range(101):
        if time == 0:
            if r < 3 and c < 3:
                if Map[r][c] == k:
                    print(0)
                    flag = 1
                    break
        else:
            if row >= column:
                if(R_calcul(time)):
                    print(time)
                    flag = 1
                    break
            else:
                if(C_calcul(time)):
                    print(time)
                    flag = 1
                    break
    if flag == 0:
        print(-1)