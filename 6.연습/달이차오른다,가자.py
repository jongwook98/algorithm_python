from sys import stdin
from collections import deque

# 열쇠를 방문하면 비트마스크로 열쇠 보유 현황을 갱신하고 방문정보를
# [y 좌표, x 좌표, 열쇠보유현황] 으로 저장하여 열쇠를 가지고 있는 순간과
# 가지고 있지 않은 순간을 구별하여 Que에 저장 탐색

N, M = map(int, stdin.readline().split())
Map = [list(stdin.readline().strip()) for _ in range(N)]

check = [[[False for _ in range(2**6)] for _ in range(M)] for _ in range(N)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

for y in range(N):
    for x in range(M):
        if Map[y][x] == '0':
            Que = deque([(y, x, 0)])
            check[y][x][0] = 0
            Map[y][x] = '.'

output = -1

while len(Que):
    cur_y, cur_x, key = Que.popleft()
    for i in range(4):
        ny = cur_y + dy[i]
        nx = cur_x + dx[i]
        if 0 <= ny < N and 0 <= nx < M:
            if Map[ny][nx] != '#' and check[ny][nx][key] is False:
                if Map[ny][nx] == '1':
                    check[ny][nx][key] = check[cur_y][cur_x][key] + 1
                    output = check[ny][nx][key]
                    Que.clear()
                    break

                elif 97 <= ord(Map[ny][nx]) <= 102:
                    Que.append((ny, nx, key | 2 ** (ord(Map[ny][nx]) - 97)))
                    check[ny][nx][key] = check[cur_y][cur_x][key] + 1
                    check[ny][nx][key | 2 ** (ord(Map[ny][nx]) - 97)] = check[cur_y][cur_x][key] + 1

                elif 65 <= ord(Map[ny][nx]) <= 70:
                    if 2 ** (ord(Map[ny][nx]) - 65) & key:
                        Que.append((ny, nx, key))
                        check[ny][nx][key] = check[cur_y][cur_x][key] + 1

                elif Map[ny][nx] == '.':
                    Que.append((ny, nx, key))
                    check[ny][nx][key] = check[cur_y][cur_x][key] + 1

print(output)

'''
# 시간 초과!
# 시간초과가 난 이유!
# 열쇠를 발견하면 재귀구조를 활용하여 다시 방문을 초기화 하고
# 문을 열어놓은 배열로 deepcopy 하여 더 많은 메모리를 사용, 같은 곳을 재방문하여
# 시간초과가 난듯 하다.

from sys import stdin
# from collections import deque
# from copy import deepcopy
N, M = map(int, stdin.readline().split())
Map = [list(stdin.readline().strip()) for _ in range(N)]

Door = [[] for _ in range(6)]
des = []

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

min_des = 10000000

for y in range(N):
    for x in range(M):
        if Map[y][x] == '0':
            SP = (y, x)
        elif 65 <= ord(Map[y][x]) <= 70:
            Door[ord(Map[y][x]) - 65].append([y, x])

def DFS(Map, move, cur_y, cur_x):
    Que = deque()
    Que.append((cur_y, cur_x))
    check = [[False] * M for _ in range(N)]
    check[cur_y][cur_x] = move
    BFS(Que, Map, check)

def BFS(Que, Map, check):
    global min_des
    while len(Que):
        cur_y, cur_x = Que.popleft()
        for i in range(4):
            ny = cur_y + dy[i]
            nx = cur_x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if check[ny][nx] is False and Map[ny][nx] == '1':
                    min_des = min(min_des, check[cur_y][cur_x] + 1)
                elif check[ny][nx] is False and Map[ny][nx] == '.':
                    Que.append((ny, nx))
                    check[ny][nx] = check[cur_y][cur_x] + 1
                elif check[ny][nx] is False and 97 <= ord(Map[ny][nx]) <= 102:
                    index = ord(Map[ny][nx]) - 97
                    Map[ny][nx] = '.'   # 열쇠 없애기
                    Map_dup = deepcopy(Map)
                    Map_dup = Open_Door(Map_dup, index)
                    DFS(Map_dup, check[cur_y][cur_x] + 1, ny, nx)

def Open_Door(Map, index):
    for i in range(len(Door[index])):
        Map[Door[index][i][0]][Door[index][i][1]] = '.'
    return Map

if __name__=="__main__":
    Que = deque()
    check = [[False] * M for _ in range(N)]
    Que.append(SP)
    check[SP[0]][SP[1]] = 0
    Map[SP[0]][SP[1]] = '.'

    BFS(Que, Map, check)
    if min_des == 10000000:
        print(-1)
    else:
        print(min_des)
'''