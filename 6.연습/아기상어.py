from sys import stdin
from collections import deque

N = int(stdin.readline())
Map = [list(map(int, stdin.readline().split())) for _ in range(N)]

# BFS로 탐지하는 먹이의 우선순위 위 왼 오 아래

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

baby_shark, intake = 2, 0
fish_size = [0 for _ in range(6)]

for y in range(N):
    for x in range(N):
        if Map[y][x] == 9:
            s_y, s_x = y, x

        elif Map[y][x] != 0:
            fish_size[Map[y][x] - 1] += 1

Map[s_y][s_x] = 0
move_Q = deque()
move_Q.append((s_y, s_x))

total_spend = 0
spend_time = [[False] * N for _ in range(N)]
spend_time[s_y][s_x] = 0

flag = fish_size[0]
score = []

eat_flag = False

while len(move_Q) and flag:
    cur_y, cur_x = move_Q.popleft()
    eating = 1
    if eat_flag is not False:
        if spend_time[cur_y][cur_x] > eat_flag or len(move_Q) == 0:
            time, s_y, s_x = max(score)

            fish_size[Map[s_y][s_x] - 1] -= 1
            Map[s_y][s_x] = 0
            intake += 1

            if intake >= baby_shark:
                baby_shark += 1
                intake = 0

            flag = 0
            for j in range(baby_shark - 1):
                if j >= 6:
                    break
                flag += fish_size[j]

            total_spend += spend_time[s_y][s_x]
            spend_time = [[False] * N for _ in range(N)]
            spend_time[s_y][s_x] = 0

            move_Q.clear()
            move_Q.append((s_y, s_x))
            eating = 0
            score = []
            eat_flag = False

    if flag and eating:
        for i in range(4):
            ny = cur_y + dy[i]
            nx = cur_x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if Map[ny][nx] <= baby_shark and spend_time[ny][nx] is False:
                    spend_time[ny][nx] = spend_time[cur_y][cur_x] + 1
                    move_Q.append((ny, nx))

                    if Map[ny][nx] < baby_shark and Map[ny][nx] != 0:
                        if eat_flag is False:
                            eat_flag = spend_time[ny][nx]

                        if spend_time[ny][nx] == eat_flag:
                            point = 100*(s_y - ny) + (s_x - nx)
                            score.append((point, ny, nx))

print(total_spend)