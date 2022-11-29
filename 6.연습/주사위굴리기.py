from sys import stdin

N, M, x, y, K = map(int, stdin.readline().split())

Map_value = [list(map(int, stdin.readline().split())) for _ in range(N)]
Move_ = list(map(int, stdin.readline().split()))

# 이동 x 동 서 북 남
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

dice_place = [1, 3, 4, 2, 5, 6] # 윗면 1 아랫면 6인 상태
dice = [0, 0, 0, 0, 0, 0] # 주사위의 규칙은 바닥면과 윗면의 합이 7

def move_dice(dice, dir):
    if dir == 1:
        dice[0], dice[1], dice[2], dice[5] = dice[2], dice[0], dice[5], dice[1]
    elif dir == 2:
        dice[0], dice[1], dice[2], dice[5] = dice[1], dice[5], dice[0], dice[2]
    elif dir == 3:
        dice[0], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[3]
    elif dir == 4:
        dice[0], dice[3], dice[4], dice[5] = dice[3], dice[5], dice[0], dice[4]

    return

for i in range(K):
    ny, nx = (y + dy[Move_[i]]), (x + dx[Move_[i]])
    if 0 <= ny < M and 0 <= nx < N:
        move_dice(dice, Move_[i])

        if Map_value[nx][ny] == 0:
            Map_value[nx][ny] = dice[5]
        else:
            dice[5] = Map_value[nx][ny]
            Map_value[nx][ny] = 0

        print(dice[0])
        y, x = ny, nx