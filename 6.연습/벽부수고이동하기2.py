from sys import stdin
from collections import deque

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

N, M, K = map(int, stdin.readline().split())
Map = [list(map(int, stdin.readline().strip())) for _ in range(N)]

check = [[[False for _ in range(M)] for _ in range(N)] for _ in range(K + 1)]

Que = deque()

Que.append((0, 0, 0))
check[0][0][0] = 1

def bfs():
    while len(Que):
        cur_y, cur_x, wall = Que.popleft()
        if cur_y == N-1 and cur_x == M-1:
            return check[wall][cur_y][cur_x]
        for i in range(4):
            ny = cur_y + dy[i]
            nx = cur_x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if check[wall][ny][nx] is False and Map[ny][nx] == 0:
                    Que.append((ny, nx, wall))
                    check[wall][ny][nx] = check[wall][cur_y][cur_x] + 1

                elif wall < K and Map[ny][nx] == 1 and check[wall + 1][ny][nx] is False:
                    Que.append((ny, nx, wall + 1))
                    check[wall + 1][ny][nx] = check[wall][cur_y][cur_x] + 1

    return -1

print(bfs())

'''
# 정답 코드인데
# 나랑 다른점(깔끔하게 정리한 것 말고 차이점)을 못찾겠다 -> 찾았다..!
# 벽을 부술 때 벽을 부순 개수를 기준으로 방문 정보를 확인 했어야 함

from collections import deque
q = deque()
from sys import stdin
input = stdin.readline

n,m,k = map(int, input().split())
vis = [[[0]*(k+1) for _ in range(m)] for __ in range(n)]
arr = [list(map(int,input().strip())) for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs() :
    q.append([0, 0, k]) # k는 벽을 뚫을 수 있는 수
    vis[0][0][k] = 1
    while q :
        x,y,z = q.popleft()
        if x == n-1 and y == m-1 :
            return vis[x][y][z]
        for i in range(4) :
            nx ,ny = dx[i] + x, dy[i] + y
            if 0<=nx<n and 0<=ny<m :
                if arr[nx][ny] == 1 and z > 0 and vis[nx][ny][z-1] == 0:
                    vis[nx][ny][z-1] = vis[x][y][z] + 1
                    q.append([nx,ny,z-1])
                elif arr[nx][ny] == 0 and vis[nx][ny][z] == 0:
                    vis[nx][ny][z] = vis[x][y][z] + 1
                    q.append([nx,ny,z])

    return -1

print(bfs())
'''