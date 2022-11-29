from copy import deepcopy

# 물고기를 복제할 때 x, y, d 에 대해서 중복되는 경우
# 배열로 추가하지말고 전체 맵에 같은 정보를 갖는 인덱스에 += 추가하면
# 같은 움직임을 같는 물고기에 대해 중복해서 계산하지 않아도 되므로 시간초과가 발생하지 않는다

mv_ = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
smv_ = [[-1, 0], [0, -1], [1, 0], [0, 1]]

Map = [[0 for _ in range(4)] for _ in range(4)]
SMap = [[0 for _ in range(4)] for _ in range(4)]
fish = [[[0 for _ in range(8)] for _ in range(4)] for _ in range(4)]

M, S = map(int, input().split())
for i in range(M):
    fx, fy, fd = map(int, input().split())
    fish[fx - 1][fy - 1][fd - 1] += 1
    Map[fx - 1][fy - 1] += 1

sx, sy = map(int, input().split())
sx, sy = sx - 1, sy - 1

dup_fish = []
score = 0


def dup():
    global dup_fish
    dup_fish = deepcopy(fish)


def fi_move():
    global fish, Map
    nfish = [[[0 for _ in range(8)] for _ in range(4)] for _ in range(4)]

    for x in range(4):
        for y in range(4):
            for d in range(8):
                if fish[x][y][d] != 0:
                    flag = True
                    for i in range(d, d - 8, -1):
                        nx, ny = x + mv_[i][0], y + mv_[i][1]
                        if (nx == sx and ny == sy) or not (0 <= nx < 4) or not (0 <= ny < 4) or SMap[nx][ny] != 0:
                            continue
                        flag = False
                        nfish[nx][ny][(i + 8) % 8] += fish[x][y][d]
                        break
                    if flag:
                        nfish[x][y][d] += fish[x][y][d]

    fish = deepcopy(nfish)
    for x in range(4):
        for y in range(4):
            Map[x][y] = sum(fish[x][y])


def sh_move():
    global sx, sy, fish

    check = [[False for _ in range(4)] for _ in range(4)]

    bt_mv = [0, 0, 0]
    b_eat = -1
    eat = 0
    for first in range(4):
        ox, oy = sx + smv_[first][0], sy + smv_[first][1]
        if 0 <= ox < 4 and 0 <= oy < 4:
            eat += Map[ox][oy]
            check[ox][oy] = True
            for second in range(4):
                tx, ty = ox + smv_[second][0], oy + smv_[second][1]
                if 0 <= tx < 4 and 0 <= ty < 4:
                    eat += Map[tx][ty]
                    check[tx][ty] = True
                    for third in range(4):
                        hx, hy = tx + smv_[third][0], ty + smv_[third][1]
                        if 0 <= hx < 4 and 0 <= hy < 4:
                            if check[hx][hy] is False:
                                eat += Map[hx][hy]

                            if eat > b_eat:
                                bt_mv = [first, second, third]
                                b_eat = eat

                            if check[hx][hy] is False:
                                eat -= Map[hx][hy]

                    eat -= Map[tx][ty]
                    check[tx][ty] = False
            eat -= Map[ox][oy]
            check[ox][oy] = False

    for y in range(4):
        for x in range(4):
            if SMap[x][y] != 0:
                SMap[x][y] -= 1

    for m in bt_mv:
        sx, sy = sx + smv_[m][0], sy + smv_[m][1]
        if Map[sx][sy] != 0:
            SMap[sx][sy] = 2
            Map[sx][sy] = 0
            for d in range(8):
                fish[sx][sy][d] = 0


def done_dup():
    global fish
    for x in range(4):
        for y in range(4):
            for d in range(8):
                fish[x][y][d] += dup_fish[x][y][d]


def sum_fish():
    global score

    for x in range(4):
        for y in range(4):
            score += sum(fish[x][y])


for _ in range(S):
    dup()
    fi_move()
    sh_move()
    done_dup()

sum_fish()
print(score)
