from sys import stdin
from collections import deque
from itertools import product
from copy import deepcopy

# 내 시간 1952ms 잘 작성한 사람의 시간 540ms
# 시간을 줄일 수 있는 방법
# 1. max 값을 찾는 과정?
# 2. DFS

# 내 방식은 중복 순열로서 반복되는 과정을 처음부터 다시 계산하고 있고
# DFS 는 해당 방향에서 계산한 값에서 여러 4방향에서 다시 사용할 수 있어
# 거의 4배 차이가 나는 듯 하다

N = int(stdin.readline())
Map_ori = [list(map(int, stdin.readline().split())) for _ in range(N)]

Que_ = [deque() for _ in range(N)]

max_block = 0
row = deque()


for pm in product((0, 1, 2, 3), repeat = 5):
    Map_ = deepcopy(Map_ori)
    for i in range(5):

        for n in range(N):
            Que_[n].clear()

        if pm[i] == 0:
            for y in range(N):
                for x in range(N):
                    if Map_[y][x] != 0:
                        Que_[x].append(Map_[y][x])

        elif pm[i] == 1:
            for y in range(N-1, -1, -1):
                for x in range(N):
                    if Map_[y][x] != 0:
                        Que_[x].append(Map_[y][x])

        elif pm[i] == 2:
            for x in range(N):
                for y in range(N):
                    if Map_[y][x] != 0:
                        Que_[y].append(Map_[y][x])

        elif pm[i] == 3:
            for x in range(N-1, -1, -1):
                for y in range(N):
                    if Map_[y][x] != 0:
                        Que_[y].append(Map_[y][x])

        Map_ = [[0 for _ in range(N)] for _ in range(N)]

        for q in range(N):
            last = 0
            while len(Que_[q]):
                cur = Que_[q].popleft()
                if last == cur:
                    cur = last + cur
                    row.pop()
                    last = 0
                else:
                    last = cur
                row.append(cur)

            cnt = 0
            while len(row):
                cur = row.popleft()
                if pm[i] == 0:
                    Map_[q][cnt] = cur
                elif pm[i] == 1:
                    Map_[q][(N-1) - cnt] = cur
                elif pm[i] == 2:
                    Map_[cnt][q] = cur
                elif pm[i] == 3:
                    Map_[(N-1) - cnt][q] = cur
                cnt += 1
    for i in range(N):
        max_block = max(max_block, max(Map_[i]))
print(max_block)
