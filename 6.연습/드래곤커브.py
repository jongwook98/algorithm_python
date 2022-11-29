from sys import stdin
from collections import deque

N = int(stdin.readline())
dragon_c = [list(map(int, stdin.readline().split())) for _ in range(N)]
Dir = deque()

dragon_c_arr = [deque() for o in range(N)]
is_arr = []

check = [[False for _ in range(101)] for _ in range(101)]
count = 0

for i in range(N):
    dragon_c_arr[i].append(dragon_c[i][2])
    x, y = dragon_c[i][0], dragon_c[i][1]
    check[x][y] = True

# 드래곤 커브의 방향
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# 사각형을 찾는 것
sx = [1, 1, 0, 0]
sy = [0, 1, 1, 0]

'''
0
0 1
0 1 2 1
0 1 2 1 2 3 2 1
0 1 2 1 2 3 2 1 2 3 4 3 2 3 2 1
'''
# 드래곤 커브의 길 찾고, check 하기

for n in range(N):
    for g in range(dragon_c[n][3]):
        Dir = dragon_c_arr[n].copy()
        while len(Dir):
            dir_ = Dir.pop()
            dragon_c_arr[n].append((dir_ + 1) % 4)

    while len(dragon_c_arr[n]):
        go_ = dragon_c_arr[n].popleft()
        x, y = dragon_c[n][0], dragon_c[n][1]

        nx, ny = x + dx[go_], y + dy[go_]

        check[nx][ny] = True
        dragon_c[n][0], dragon_c[n][1] = nx, ny

# 마지막 정사각형 개수 세는 것!
for x in range(100):
    for y in range(100):
        square = 1
        for i in range(4):
            if 0 <= x+sx[i] <= 100 and 0 <= y+sy[i] <= 100:
                if check[x+sx[i]][y+sy[i]] is False:
                    square = 0
                    break
        if square == 1:
            count += 1

print(count)