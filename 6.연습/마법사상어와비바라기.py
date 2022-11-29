from sys import stdin

move_ = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
diag = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
order = []

N, M = map(int, stdin.readline().split())
Map = [list(map(int, stdin.readline().split())) for _ in range(N)]

check = [[False for _ in range(N)] for _ in range(N)]
for _ in range(M):
    d, s = map(int, stdin.readline().split())
    order.append([d - 1, s])

cloud = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
rain_cloud = []
SUM_ = 0

def gen_cloud():
    global check, Map, cloud
    cloud.clear()
    for y in range(N):
        for x in range(N):
            if check[y][x] is False and Map[y][x] >= 2:
                Map[y][x] -= 2
                check[y][x] = True
                cloud.append([y, x])

def dup_water(rain):
    global check, Map
    check = [[False for _ in range(N)] for _ in range(N)]

    for cy, cx in rain:
        check[cy][cx] = True
        for i in range(4):
            ny, nx = cy + diag[i][0], cx + diag[i][1]
            if 0 <= ny < N and 0 <= nx < N:
                if Map[ny][nx] != 0:
                    Map[cy][cx] += 1

    gen_cloud()

def move_cloud(d, s):
    global cloud, Map, rain_cloud
    index = s % N
    rain_cloud.clear()

    for cy, cx in cloud:
        ny, nx = (N + cy + move_[d][0] * index) % N, (N + cx + move_[d][1] * index) % N
        Map[ny][nx] += 1
        rain_cloud.append([ny, nx])

    dup_water(rain_cloud)

def SUM_cloud():
    global SUM_
    for i in range(N):
        SUM_ += sum(Map[i])

if __name__=='__main__':
    for d, s in order:
        move_cloud(d, s)

    SUM_cloud()
    print(SUM_)