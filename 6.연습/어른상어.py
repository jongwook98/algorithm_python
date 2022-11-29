from sys import stdin

# 그냥 구현 문제

# 구현은 성공했다만
# 변수를 선언할 때 생각좀 하고 선언해야 할듯
# 너무 복잡해서 헷갈린다

N, M, k = map(int, stdin.readline().split())

position = []
base_Map = [list(map(int, stdin.readline().split())) for _ in range(N)]
Map = [[[0, 0] for _ in range(N)] for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for i in range(N):
    for j in range(N):
        if base_Map[i][j] != 0:
            position.append([base_Map[i][j], i, j])
            Map[i][j] = [base_Map[i][j], 0]

position.sort()
dir = list(map(int, stdin.readline().split()))
move = [[list(map(int, stdin.readline().split())) for _ in range(4)] for _ in range(M)]

for i in range(M):
    dir[i] = dir[i] - 1

for i in range(M):
    for j in range(4):
        for v in range(4):
            move[i][j][v] = move[i][j][v] - 1

for i in range(len(position)):
    Map[position[i][1]][position[i][2]][0] = position[i][0]
    Map[position[i][1]][position[i][2]][1] = k

def shark_move(Map, position, dir, move):

    for Time in range(1, 1001):
        check = [[0] * N for _ in range(N)]
        contact = []

        for i in range(len(position)):
            shark_num, y, x = position[i][0], position[i][1], position[i][2]
            cur_dir = dir[shark_num -1]
            flag = 0

            for j in move[shark_num-1][cur_dir]:
                ny = y + dy[j]
                nx = x + dx[j]

                if 0 <= ny < N and 0 <= nx < N:
                    if Map[ny][nx][0] == 0:
                        flag = 1
                        position[i][1] = ny
                        position[i][2] = nx
                        dir[shark_num - 1] = j

                        if check[ny][nx] != 0 and (ny, nx) not in contact:
                            contact.append((ny, nx))
                        check[ny][nx] += 2 ** (shark_num-1)

                        break
            if flag == 0:
                for j in move[shark_num-1][cur_dir]:
                    ny = y + dy[j]
                    nx = x + dx[j]
                    if 0 <= ny < N and 0 <= nx < N:
                        if Map[ny][nx][0] == shark_num:

                            position[i][1] = ny
                            position[i][2] = nx
                            dir[shark_num - 1] = j

                            break

        for Map_y in range(N):
            for Map_x in range(N):
                if Map[Map_y][Map_x][1] != 0:
                    Map[Map_y][Map_x][1] -= 1
                    if Map[Map_y][Map_x][1] == 0:
                        Map[Map_y][Map_x][0] = 0

        for i in range(len(contact)):
            cont_y, cont_x = contact[i][0], contact[i][1]
            con_flag = 0
            erase_position = []

            for j in range(len(position)):
                if [position[j][0], cont_y, cont_x] in position:
                    if con_flag == 1:
                        erase_position.append([position[j][0], cont_y, cont_x])
                    else:
                        con_flag = 1

            for j in erase_position:
                position.remove(j)

        if len(position) == 1:
            return Time

        for i in range(len(position)):
            Map[position[i][1]][position[i][2]][0] = position[i][0]
            Map[position[i][1]][position[i][2]][1] = k

        if Time >= 1000:
            return -1

print(shark_move(Map, position, dir, move))