from sys import stdin
from collections import deque

# 벽을 세우는 모든 경우에 대해서 해보자?

N, M = map(int, stdin.readline().split())
lab_map = [[] for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

max_count = 0
virus_init = []

for i in range(N):
    lab_map[i] = list(map(int, stdin.readline().split()))
for y in range(N):
    for x in range(M):
        if lab_map[y][x] == 2:
            virus_init.append((y, x))


# 여기서 부터 브루트 포스 (벽 세우고 아래 시작)
for one in range(N*M-2):
    one_x = one % M
    one_y = one // M
    if lab_map[one_y][one_x] != 0:
        continue

    for two in range(one + 1, N*M-1):
        two_x = two % M
        two_y = two // M
        if lab_map[two_y][two_x] != 0:
            continue

        for three in range(two + 1, N*M):
            three_x = three % M
            three_y = three // M
            if lab_map[three_y][three_x] != 0:
                continue

            lab_map_dup = [] + lab_map

            lab_map_dup[three_y][three_x] = 1
            lab_map_dup[two_y][two_x] = 1
            lab_map_dup[one_y][one_x] = 1

            print(lab_map)

            count = 0
            Que = deque(virus_init)
            check = [[False for _ in range(M)] for _ in range(N)]

            while len(Que):
                cur_y, cur_x = Que.popleft()
                for i in range(4):
                    nx = cur_x + dx[i]
                    ny = cur_y + dy[i]
                    if 0 <= nx < M and 0 <= ny < N:
                        if lab_map_dup[ny][nx] == 0 and check[ny][nx] == False:
                            Que.append((ny, nx))
                            lab_map_dup[ny][nx] = 2
                            check[ny][nx] = True

            for y in range(N):
                for x in range(M):
                    if lab_map_dup[y][x] == 0:
                        count = count + 1

            max_count = max(max_count, count)
            print(lab_map)

print(max_count)