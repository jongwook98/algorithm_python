from sys import stdin
from collections import deque
from collections import defaultdict

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

N, M, GAS = map(int, stdin.readline().split())
Map = [list(stdin.readline().split()) for _ in range(N)]

st_y, st_x = map(int, stdin.readline().split())
client = defaultdict(list)

for _ in range(M):
    cl_y, cl_x, des_y, des_x = map(int, stdin.readline().split())
    client[(cl_y - 1, cl_x - 1)] = [des_y - 1, des_x - 1]

def find_shortest_path(st_y, st_x):
    global client
    global GAS

    if (st_y, st_x) in client.keys():
        des_y, des_x = client[(st_y, st_x)]
        del client[(st_y, st_x)]
        return go_des(st_y, st_x, des_y, des_x)

    check = [[False for _ in range(N)] for _ in range(N)]
    Que = deque([[st_y, st_x]])
    check[st_y][st_x] = GAS
    candi = []
    short_des = False

    while len(Que):
        cur_y, cur_x = Que.popleft()
        if len(candi) and check[cur_y][cur_x] <= short_des:
            candi.sort()
            del client[(candi[0][2], candi[0][3])]
            GAS = check[candi[0][2]][candi[0][3]]

            return go_des(candi[0][2], candi[0][3], candi[0][4], candi[0][5])

        for i in range(4):
            ny = cur_y + dy[i]
            nx = cur_x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if check[ny][nx] is False and Map[ny][nx] == '0':
                    check[ny][nx] = check[cur_y][cur_x] - 1
                    if check[ny][nx] <= -1:
                        return print(-1)
                    Que.append([ny, nx])

                    if (ny, nx) in client.keys():
                        if short_des is False:
                            short_des = check[ny][nx]
                        point = ny * 100 + nx
                        des_y, des_x = client[(ny, nx)]
                        candi.append([point, check[ny][nx], ny, nx, des_y, des_x])
    return print(-1)

def go_des(st_y, st_x, des_y, des_x):
    global GAS
    global client

    Que = deque([[st_y, st_x]])
    check = [[False for _ in range(N)] for _ in range(N)]
    check[st_y][st_x] = GAS

    while len(Que):
        cur_y, cur_x = Que.popleft()
        for i in range(4):
            ny = cur_y + dy[i]
            nx = cur_x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if check[ny][nx] is False and Map[ny][nx] == '0':
                    check[ny][nx] = check[cur_y][cur_x] - 1
                    if check[ny][nx] <= -1:
                        return print(-1)
                    Que.append([ny, nx])

                    if (ny, nx) == (des_y, des_x):
                        GAS = check[ny][nx] + (check[st_y][st_x] - check[ny][nx]) * 2
                        if len(client):
                            return find_shortest_path(ny, nx)
                        else:
                            return print(GAS)

    return print(-1)

if __name__=="__main__":
    find_shortest_path(st_y - 1, st_x - 1)


'''
from sys import stdin
from collections import deque
from collections import defaultdict

# BFS 탐색 시 위 왼 오 아래로는 같은 거리에서 행이 낮은 것, 열이 낮은 것을 찾을 수 없음

# 택시 시작지점과 손님이 바로 있는 경우,,,

# 택시 목적지와, 손님이 있는 경우 -> 이건 된듯


dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

N, M, GAS = fuel = map(int, stdin.readline().split())
Map = [list(map(int, stdin.readline().split())) for _ in range(N)]
check = [[False for _ in range(N)] for _ in range(N)]

Que = deque()

start = list(map(int, stdin.readline().split()))
Que.append([start[0] - 1, start[1] - 1]) #좌표y 좌표x, 연료, 태우고 나서 소모 연료

client = []
des = []
client = defaultdict(list)

for _ in range(M):
    info = list(map(int, stdin.readline().split()))
    client[(info[0] - 1, info[1] - 1)].append((info[2] - 1, info[3] - 1))

def BFS():
    global GAS
    global check
    des_flag = [(False, False)]
    start_flag = [False, False]

    while len(Que):
        cur_y, cur_x = Que.popleft()
        flag = 0

        for i in range(4):
            if flag == 1:
                break

            ny = cur_y + dy[i]
            nx = cur_x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if check[ny][nx] is False and Map[ny][nx] == 0:
                    check[ny][nx] = check[cur_y][cur_x] - 1
                    if check[ny][nx] < 0:
                        return print(-1)

                    Que.append([ny, nx])
                    if [(ny, nx)] == des_flag:

                        GAS = check[ny][nx] + (check[start_flag[0]][start_flag[1]] - check[des_flag[0][0]][des_flag[0][1]]) * 2

                        if len(client) == 0:
                            return print(GAS)

                        check = [[False for _ in range(N)] for _ in range(N)]
                        check[ny][nx] = GAS

                        start_flag = [False, False]
                        des_flag = [(False, False)]

                        Que.clear()
                        Que.append([ny, nx])

                        flag = 1

                    if (ny, nx) in client.keys() and start_flag == [False, False]:
                        start_flag = [ny, nx]
                        des_flag = client[(ny, nx)]

                        del client[(ny, nx)]
                        GAS = check[ny][nx]

                        check = [[False for _ in range(N)] for _ in range(N)]
                        check[ny][nx] = GAS
                        Que.clear()
                        Que.append([ny, nx])

                        flag = 1

    return print(-1)

if __name__=="__main__":
    BFS()
'''