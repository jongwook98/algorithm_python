from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
Map = [list(map(int, stdin.readline().split())) for _ in range(N)]

count = 0
virus = []

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

min_output = 1000000

for y in range(N):
    for x in range(N):
        if Map[y][x] == 0:
            count += 1
        elif Map[y][x] == 2:
            virus.append([y, x])

def select_virus(sel_virus, index, num):
    if num >= M:
        return bfs(sel_virus)
    elif index >= len(virus):
        return False

    sel_virus.append(virus[index])
    select_virus(sel_virus, index + 1, num + 1)
    sel_virus.pop()
    select_virus(sel_virus, index + 1, num)

def bfs(sel_virus):
    global min_output

    Que = deque()
    check = [[False for _ in range(N)] for _ in range(N)]

    for i in range(len(sel_virus)):
        Que.append([sel_virus[i][0], sel_virus[i][1]])
        check[sel_virus[i][0]][sel_virus[i][1]] = 0

    count_dub = count
    while len(Que):
        cur_y, cur_x = Que.popleft()
        for i in range(4):
            ny = cur_y + dy[i]
            nx = cur_x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if check[ny][nx] is False and Map[ny][nx] == 0:
                    check[ny][nx] = check[cur_y][cur_x] + 1
                    Que.append([ny, nx])
                    count_dub -= 1

                    if count_dub == 0:
                        output = check[ny][nx]
                        min_output = min(min_output, output)
                        Que.clear()

                if check[ny][nx] is False and Map[ny][nx] == 2:
                    check[ny][nx] = check[cur_y][cur_x] + 1
                    Que.append([ny, nx])

if __name__=="__main__":
    if count == 0:
        print(0)
    else:
        select_virus(list(), 0, 0)
        if min_output == 1000000:
            print(-1)
        else:
            print(min_output)