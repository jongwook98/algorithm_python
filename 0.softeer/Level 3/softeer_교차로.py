from sys import stdin
from collections import deque

N = int(stdin.readline())
car_arr = [list(stdin.readline().split()) for _ in range(N)]

Que_ = [deque() for _ in range(4)]
time_table = deque()

for n in range(N):
    Que_[(ord(car_arr[n][1]) - 65)].append((int(car_arr[n][0]), n))
    time_table.append(int(car_arr[n][0]))

time = time_table[0]
output_arr = [-1 for _ in range(N)]

INF = int(2e9)

while True:
    flag = 0

    A_t = Que_[0][0][0] if len(Que_[0]) else INF
    B_t = Que_[1][0][0] if len(Que_[1]) else INF
    C_t = Que_[2][0][0] if len(Que_[2]) else INF
    D_t = Que_[3][0][0] if len(Que_[3]) else INF

    min_time = min(A_t, B_t, C_t, D_t)
    if min_time > time: time = min_time

    for i in range(4):
        if len(Que_[(i%4)]):
            if Que_[(i%4)][0][0] <= time:
                if len (Que_[((i+3)%4)]):
                    if Que_[((i+3)%4)][0][0] <= time:
                        continue
                    else:
                        flag += 2 ** i
                else:
                    flag += 2 ** i

    if flag == 0:
        break

    for i in range(4):
        if flag & (2 ** i):
            tra, index = Que_[i].popleft()
            output_arr[index] = time
            time_table.popleft()

    time += 1

for i in range(N):
    print(output_arr[i])