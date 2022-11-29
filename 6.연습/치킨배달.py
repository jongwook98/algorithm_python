from sys import stdin

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

N, M = map(int, stdin.readline().split())
map_arr = [list(map(int, stdin.readline().split())) for _ in range(N)]

Init_chicken = []
select_chicken = []

Init_house = []

repetition = 1
repetition_fraction = 1

for y in range(N):
    for x in range(N):
        if map_arr[y][x] == 2:
            Init_chicken.append((y, x))
        if map_arr[y][x] == 1:
            Init_house.append((y, x))

min_dis = 10000000

def make_permanaunt(num, count, chicken_arr, Init_chicken, M):
    global min_dis

    if count == M:
        min_dis_arr = [10000 for _ in range(len(Init_house))]

        for i in range(M):
            for cnt, house in enumerate(Init_house):
                min_dis_arr[cnt-1] = min(min_dis_arr[cnt-1], (abs(Init_chicken[chicken_arr[i]][0] - house[0]) + abs(Init_chicken[chicken_arr[i]][1] - house[1])))

        min_dis = min(min_dis, sum(min_dis_arr))
        return

    if len(Init_chicken) - num - (M - count) <= -1:
        return

    make_permanaunt(num + 1, count, chicken_arr, Init_chicken, M)
    chicken_arr.append(num)
    make_permanaunt(num + 1, count + 1, chicken_arr, Init_chicken, M)
    chicken_arr.pop()

make_permanaunt(0, 0, select_chicken, Init_chicken, M)

print(min_dis)
