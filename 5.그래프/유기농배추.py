# 이중 for 문으로 Que에 넣는다. -> check True일 때는 continue
# BFS를 이용해여 인접한 배추 check True로 만들기

from sys import stdin
from collections import deque

Test_case = int(stdin.readline())

for _ in range(Test_case):
    M, N, K = map(int, stdin.readline().split())

    Que = deque()

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    cabbage = [[0 for _ in range(N)] for _ in range(M)]
    check = [[False for _ in range(N)] for _ in range(M)]
    count = 0

    for _ in range(K):
        x, y = map(int, stdin.readline().split())
        cabbage[x][y] = 1

    for x in range(M):
        for y in range(N):
            if cabbage[x][y] == 1 and check[x][y] == False:
                Que.append((x, y))
                count = count + 1

            while len(Que):
                cur_x, cur_y = Que.popleft()

                check[cur_x][cur_y] = True
                for i in range(4):
                    nx = cur_x + dx[i]
                    ny = cur_y + dy[i]
                    if 0 <= nx < M and 0 <= ny < N:
                        if cabbage[nx][ny] == 1 and check[nx][ny] == False:
                            Que.appendleft((nx, ny))
                            check[nx][ny] = True

    print(count)