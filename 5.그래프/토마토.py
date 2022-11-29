# 시간 초과가 난 이유 -> list.pop(0) 은 시간 복잡도가 O(N)이기 때문에
# 0번째 인덱스를 pop하고 싶은 경우는 collections 의 deque 구조를 사용하여 popleft() 함수를 이용한다 -> 시간복잡도 O(1)
# DFS의 stack 을 사용할 경우 list의 pop 위치가 오른쪽이기 때문에 list.pop() 은 시간 복잡도 O(1) 그대로 사용 가능하다.

from sys import stdin
from collections import deque

M, N = map(int, stdin.readline().split())
tomato = [[] for _ in range(N)]
spread_y = []
spread_x = []
count = 0 # 안익은 토마토 남은 개수
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

for i in range(N):
    tomato[i] = list(map(int, stdin.readline().split()))

Que = deque()

for Y in range(N):
    for X in range(M):
        if tomato[Y][X] == 1:
            Que.append((Y, X))
        elif tomato[Y][X] == 0:
            count += 1

while Que:
    cur_y, cur_x = Que.popleft()

    for i in range(4):
        ny = cur_y + dy[i]
        nx = cur_x + dx[i]
        if 0 <= ny < N and 0 <= nx < M:
            if tomato[ny][nx] == 0:
                Que.append((ny, nx))
                tomato[ny][nx] = tomato[cur_y][cur_x] + 1
                count -= 1

if count == 0:
    print(tomato[cur_y][cur_x] - 1)
else:
    print(-1)

'''
시간초과가 난 이유 -> list.pop(0) 은 시간복잡도가 O(N)이기 때문에
0번째 인덱스를 pop하고 싶은 경우는 collections 의 deque 구조를 사용하여 popleft() 함수를 이용한다 -> 시간복잡도 O(1)

M, N = map(int, stdin.readline().split())
tomato = [[] for _ in range(N)]
spread_y = []
spread_x = []
count = 0 # 안익은 토마토 남은 개수
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

for i in range(N):
    tomato[i] = list(map(int, stdin.readline().split()))

for Y in range(N):
    for X in range(M):
        if tomato[Y][X] == 1:
            spread_y.append(Y)
            spread_x.append(X)
        elif tomato[Y][X] == 0:
            count += 1

Que_y = spread_y
Que_x = spread_x

while Que_y:
    cur_y = Que_y[0]
    cur_x = Que_x[0]
    for i in range(4):
        ny = cur_y + dy[i]
        nx = cur_x + dx[i]
        if 0 <= ny < N and 0 <= nx < M:
            if tomato[ny][nx] == 0:
                Que_y.append(ny)
                Que_x.append(nx)
                tomato[ny][nx] = tomato[cur_y][cur_x] + 1
                count -= 1

    Que_y.pop(0)
    Que_x.pop(0)

if count == 0:
    print(tomato[cur_y][cur_x] - 1)
else:
    print(-1)
'''