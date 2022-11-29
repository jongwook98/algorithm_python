from sys import stdin
from collections import deque

N, M, T = map(int, stdin.readline().split())

circle = [deque(list(map(int, stdin.readline().split()))) for _ in range(N)]
circle = [[]] + circle

move = [list(map(int, stdin.readline().split())) for _ in range(T)]

def rotate(x, d, k):
    global circle
    for i in range(x, N+1, x):
        if d == 0:
            for _ in range(k):
                circle[i].appendleft(circle[i].pop())
        else:
            for _ in range(k):
                circle[i].append(circle[i].popleft())

    check = [[False for _ in range(M)] for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(M):
            if circle[i][j] == 0:
                continue
            if i != N:
                if circle[i][j] == circle[i + 1][j]:
                    check[i][j], check[i + 1][j] = True, True
            if circle[i][j] == circle[i][j - 1]:
                check[i][j], check[i][j - 1] = True, True

    flag = 0

    sum_, index_ = 0, 0
    for i in range(1, N + 1):
        for j in range(M):
            if check[i][j] is True:
                circle[i][j] = 0
                flag = 1
            elif circle[i][j] != 0:
                sum_ += circle[i][j]
                index_ += 1

    if flag == 0:
        if index_ != 0:
            ave = sum_ / index_
            for i in range(1, N + 1):
                for j in range(M):
                    if circle[i][j] != 0:
                        if circle[i][j] > ave:
                            circle[i][j] -= 1
                        elif circle[i][j] < ave:
                            circle[i][j] += 1

for x, d, k in move:
    rotate(x, d, k)

sum_ = 0
for i in range(1, N+1):
    sum_ += sum(circle[i])

print(sum_)