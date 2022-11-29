# 낮 과 밤을 따로 저장하여 deque 에 저장하면 시간초과가 발생한다..
# 벽 부수고 이동하기 2 의 해결 시간이 7000ms 를 생각하면
# 배열이 2배가 되었을 때 걸리는 시간은 약 10초를 넘어가서
# 배열을 늘려서 해결하는 방법은 안되는 듯 하다...

'''
from sys import stdin
from collections import deque

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

N, M, K = map(int, stdin.readline().split())
Map = [list(map(int, stdin.readline().strip())) for _ in range(N)]

check = [[[[False for _ in range(M)] for _ in range(N)] for _ in range(2)] for _ in range(K + 1)]

Que = deque()
Que.append([0, 0, 0, 0])
check[0][0][0][0] = 1

def bfs():
    while len(Que):
        cur_y, cur_x, time, wall = Que.popleft()

        if cur_y == N - 1 and cur_x == M - 1:

        # # 디버그
        #     for w in range(K + 1):
        #         for t in range(2):
        #             for y in range(N):
        #                 print(check[w][t][y])
        #             print()
        # # 디버그

            return check[wall][time][cur_y][cur_x]

        if time == 1 and check[wall][1 - time][cur_y][cur_x] is False:
            Que.append([cur_y, cur_x, 1 - time, wall])
            check[wall][1 - time][cur_y][cur_x] = check[wall][time][cur_y][cur_x] + 1

        for i in range(4):
            ny, nx = cur_y + dy[i], cur_x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if Map[ny][nx] == 0 and check[wall][1 - time][ny][nx] is False:
                    Que.append([ny, nx, 1 - time, wall])
                    check[wall][1 - time][ny][nx] = check[wall][time][cur_y][cur_x] + 1

                elif time == 0 and Map[ny][nx] == 1 and wall < K and check[wall + 1][time][ny][nx] is False and check[wall + 1][1 - time][ny][nx] is False:
                    Que.append([ny, nx, 1 - time, wall + 1])
                    check[wall + 1][1][ny][nx] = check[wall][time][cur_y][cur_x] + 1

    return -1

print(bfs())
'''

'''
# 이 문제를 풀면서 깨달은 점,,

# 같은 BFS 문제라도 특정 조건에 의해서 많은 것을 변경, 추가 조치를 해줘야 함
-> BFS 한 사이클 (이동 거리에 대한 것)

# 방문정보를 어떻게 작성할것인지에 대한 생각 등등

from sys import stdin
from collections import deque

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

N, M, K = map(int, stdin.readline().split())
Map = [list(map(int, stdin.readline().strip())) for _ in range(N)]

check = [[[False for _ in range(M)] for _ in range(N)] for _ in range(K + 1)]

Que = deque()
Que.append([0, 0, 0, 1])
check[0][0][0] = True

def bfs():
    day = True
    while len(Que):
        rep = len(Que)
        for _ in range(rep):
            cur_y, cur_x, wall, dis = Que.popleft()
            if cur_y == N - 1 and cur_x == M - 1:
                return dis

            for i in range(4):
                ny, nx = cur_y + dy[i], cur_x + dx[i]
                if 0 <= ny < N and 0 <= nx < M:
                    if Map[ny][nx] == 0 and check[wall][ny][nx] is False:
                        Que.append([ny, nx, wall, dis + 1])
                        check[wall][ny][nx] = True

                    elif Map[ny][nx] == 1 and wall < K and check[wall + 1][ny][nx] is False:
                        if day:
                            Que.append([ny, nx, wall + 1, dis + 1])
                            check[wall + 1][ny][nx] = True
                        elif check[wall][cur_y][cur_x] != 2:
                            Que.append([cur_y, cur_x, wall, dis + 1])
                            check[wall][cur_y][cur_x] = 2
        day = not day
    return -1

print(bfs())
'''

# 구글링에서 얻은 정답 코드 무료 평균보다 1/3 의 시간만 걸렸다....!
# 다른점이 뭘까...??
# 정말,, 시간초과 문제가 많이 뜬 문제,,

# 거리가 1 인 BFS 사이클은 어차피 이전 BFS 사이클에 의해 정해지므로
# 해당 사이클의 시간 낮 과 밤을 고려할 필요 없고 다음 BFS 사이클이 들어오면 시간을 변화시켜주면 됨,,,
# -> BFS 사이클의 수는 반복문안에 BFS 길이 만큼 반복시키면 사이클만큼 반복할 수 있음..

# 방문정보를 벽의 최대 수 + 1 로 저장하여 방문하기까지 허문 벽의 수를 제한하여쏘
# 방문정보를 허문 벽의 수로 한 이유는 해당 지점까지 가는데 허문벽의 수를 기록,
# 더 적게 허물어서 도착한 경우 다시 Que 구조에 넣어서 확인할 수 있도록 설계..

# 마찬가지로 내가 겪은 시간초과 문제 (다음 이동이 벽일 때 중복 방문 체크) 도 방문정보 <= w 에 의해 백트래킹 된다,,
# 그리고 거리가 1이고 이동시간도 1로 동일하므로 사이클이 지나고 +1 해주면 똑같음 -> 메모리를 추가로 사용하지 않아 메모리 초과가 발생하지 않음

import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())

if n == m == 1:
    print(1)
    exit()

road = [[c for c in input()] for _ in range(n)]

visited = [[k + 1 for _ in range(m)] for _ in range(n)]
visited[0][0] = 0
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
q = deque([(0, 0, 0)])
res = 1

is_night = False
while q:
    q_length = len(q) 
    for _ in range(q_length):
        r, c, w = q.popleft()
        
        if r == n - 1 and c == m - 1:
            print(res)

            for y in range(n):
                print(visited[y])

            exit()

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            if not(0 <= nr < n and 0 <= nc < m):
            # 맵의 범위를 벗어난다면
                continue
                
            if visited[nr][nc] <= w: 
            # 이미 더 적은 방법으로 도달할 수 있다면
                continue

            # 밤이 아니고
            if not is_night:
                if road[nr][nc] == '0': # 갈 수 있는 길이라면
                    visited[nr][nc] = w
                    q.append((nr, nc, w))
                else:
                    if w >= k: 
                        continue
                    visited[nr][nc] = w
                    q.append((nr, nc, w + 1))
            else:
                if road[nr][nc] == '0':
                    visited[nr][nc] = w
                    q.append((nr, nc, w))
                else:
                    q.append((r, c, w))

    is_night = not is_night
    res += 1

print(-1)