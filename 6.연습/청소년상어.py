from sys import stdin
from copy import deepcopy

# DFS를 활용하여 문제를 풀었다.
# DFS로 깊게 들어갈 수록 원본 데이터를 보존하는 것을 deep copy로 했다.

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -2, -2, -2, 0, 2, 2, 2]

Max_score = 0

def move_fish(Map, fish_arr):
    for i in range(len(fish_arr)):
        fc_dir, (fc_y, fc_x) = fish_arr[i][1], fish_arr[i][2]

        for j in range(8):
            fn_dir = (fc_dir + j) % 8
            fn_y = fc_y + dy[fn_dir]
            fn_x = fc_x + dx[fn_dir]
            if 0 <= fn_y < 4 and 0 <= fn_x < 8:
                if Map[fn_y][fn_x] != 44:
                    if Map[fn_y][fn_x] != 0:
                        index_last = fish_arr.index((Map[fc_y][fc_x], Map[fc_y][fc_x + 1], (fc_y, fc_x)))
                        index_next = fish_arr.index((Map[fn_y][fn_x], Map[fn_y][fn_x + 1], (fn_y, fn_x)))

                        Map[fc_y][fc_x], Map[fn_y][fn_x] = Map[fn_y][fn_x], Map[fc_y][fc_x]
                        Map[fc_y][fc_x + 1], Map[fn_y][fn_x + 1] = Map[fn_y][fn_x + 1], fn_dir

                        fish_arr[index_last] = fish_arr[index_last][0], fn_dir, (fn_y, fn_x)
                        fish_arr[index_next] = fish_arr[index_next][0], Map[fc_y][fc_x + 1], (fc_y, fc_x)

                    else:
                        index_base = fish_arr.index((Map[fc_y][fc_x], Map[fc_y][fc_x + 1], (fc_y, fc_x)))

                        Map[fc_y][fc_x], Map[fn_y][fn_x] = 0, Map[fc_y][fc_x]
                        Map[fc_y][fc_x + 1], Map[fn_y][fn_x + 1] = 0, fn_dir

                        fish_arr[index_base] = fish_arr[index_base][0], fn_dir, (fn_y, fn_x)

                    break

    return Map

def shark_move(Map, shark, fish_arr, score):
    global Max_score

    for i in range(1, 4):
        ny = shark[0] + i * dy[shark[2]]
        nx = shark[1] + i * dx[shark[2]]
        if 0 <= ny < 4 and 0 <= nx < 8:
            if Map[ny][nx] != 0:
                Map_dup = deepcopy(Map)
                fish_arr_dup = deepcopy(fish_arr)
                shark_dup = deepcopy(shark)

                eating_fish = Map_dup[ny][nx]
                score += eating_fish

                fish_arr_dup.remove((Map_dup[ny][nx], Map_dup[ny][nx+1], (ny, nx)))
                Map_dup[shark_dup[0]][shark_dup[1]], Map_dup[ny][nx] = 0, 44
                shark_dup = [ny, nx, Map_dup[ny][nx + 1]]

                Map_dup = move_fish(Map_dup, fish_arr_dup)
                shark_move(Map_dup, shark_dup, fish_arr_dup, score)
                score -= eating_fish

    Max_score = max(Max_score, score)

if __name__=="__main__":

    Map = [list(map(int, stdin.readline().split())) for _ in range(4)]
    fish_arr = []

    for y in range(4):
        for x in range(4):
            if y == 0 and x == 0:
                Map[y][2 * x + 1] = Map[y][2 * x + 1] - 1
            else:
                Map[y][2 * x + 1] = Map[y][2 * x + 1] - 1
                fish_arr.append((Map[y][2 * x], Map[y][2 * x + 1], (y, x * 2)))

    fish_arr.sort()

    Max_score = 0
    score = Map[0][0]

    shark = [0, 0, Map[0][1]] # y, x, dir
    Map[0][0] = 44  # 상어는 44

    Map = move_fish(Map, fish_arr)

    shark_move(Map, shark, fish_arr, score)

    print(Max_score)