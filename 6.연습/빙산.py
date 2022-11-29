from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def count_contact(Map, time):
    Que = deque()
    check = [[False for _ in range(M)] for _ in range(N)]
    contact_Map = [[0 for _ in range(M)] for _ in range(N)]

    count = 0

    for y in range(N):
        for x in range(M):
            if Map[y][x] != 0 and check[y][x] is False:
                if count == 1:
                    return time
                count = 1
                Que.append((y, x))
                check[y][x] = True
                while len(Que):
                    cur_y, cur_x = Que.popleft()
                    for i in range(4):
                        ny = cur_y + dy[i]
                        nx = cur_x + dx[i]
                        if 0 <= ny < N and 0 <= nx < M:
                            if Map[ny][nx] != 0 and check[ny][nx] is False:
                                check[ny][nx] = True
                                Que.append((ny, nx))
                            elif Map[ny][nx] == 0:
                                contact_Map[cur_y][cur_x] += 1

    if count == 0:
        return 0
    else:
        return melt_ice(Map, contact_Map, time)

def melt_ice(Map, contact_Map, time):
    for y in range(N):
        for x in range(M):
            if contact_Map[y][x] != 0:
                Map[y][x] -= contact_Map[y][x]
                if Map[y][x] < 0:
                    Map[y][x] = 0

    return count_contact(Map, time+1)

if __name__=="__main__":
    Map = [list(map(int, stdin.readline().split())) for _ in range(N)]
    print(count_contact(Map, 0))