from sys import stdin

dy = [[-1, 1, -2, 2, 0, -1, 1, -1, 1],
      [0, 0, 1, 1, 3, 1, 1, 2, 2],
      [-1, 1, -2, 2, 0, -1, 1, -1, 1],
      [0, 0, -1, -1, -3, -1, -1, -2, -2]
      ]

dx = [[0, 0, -1, -1, -3, -1, -1, -2, -2],
      [-1, 1, -2, 2, 0, -1, 1, -1, 1],
      [0, 0, 1, 1, 3, 1, 1, 2, 2],
      [-1, 1, -2, 2, 0, -1, 1, -1, 1]
      ]

per = [0.01, 0.01, 0.02, 0.02, 0.05, 0.07, 0.07, 0.1, 0.1]

di = [[0, -1], [1, 0], [0, 1], [-1, 0]]
cd = 0

sand_out = 0

N = int(stdin.readline().strip())
Map = [list(map(int, stdin.readline().split())) for _ in range(N)]
check = [[False for _ in range(N)] for _ in range(N)]

SP = [N//2, N//2]
check[SP[0]][SP[1]] = True

def tornado():
    global cd, check, sand_out, SP, Map
    y, x = SP
    move_ = 0

    while True:
        move_ += 1
        ny = y + di[cd][0] * move_
        nx = x + di[cd][1] * move_

        by = ny - di[cd][0]
        bx = nx - di[cd][1]

        nny = y + di[cd][0] * (move_ + 1)
        nnx = x + di[cd][1] * (move_ + 1)

        # debug
        # print(move_, ny, by, nx, bx, SP)
        # for t in range(N):
        #     print(Map[t])

        if 0 <= ny < N and 0 <= nx < N:
            check[ny][nx] = True
        else:
            break

        cur_sand = Map[ny][nx]
        total_sand = Map[ny][nx]
        SP = [ny, nx]

        #print(sand_out, cur_sand, total_sand)

        Map[ny][nx] = 0

        for i in range(9):
            to_y = by + dy[cd][i]
            to_x = bx + dx[cd][i]

            to_sand = int(total_sand * per[i])

            if to_sand > 0:
                if 0 <= to_y < N and 0 <= to_x < N:
                    #print(to_sand, i, to_y, to_x)
                    Map[to_y][to_x] += to_sand
                    cur_sand -= to_sand
                else:
                    sand_out += to_sand
                    cur_sand -= to_sand

        if 0 <= nny < N and 0 <= nnx < N:
            Map[nny][nnx] += cur_sand

        else:
            sand_out += cur_sand

        if SP == [0, 0]:
            break

        if check[ny + di[cd-3][0]][nx + di[cd-3][1]] is False:
            cd += 1
            cd %= 4
            break

while not (SP[0] == 0 and SP[1] == 0):
    tornado()

#print(Map)
print(sand_out)