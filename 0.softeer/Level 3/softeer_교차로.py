# 특정상황에서 시간초과가 나는 오류가 있다
# 현재는 40/100 점 코드

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

while True:
    flag = 0

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

    if flag == 0 and time >= time_table[-1]:
        break
    if flag == 0:
        time = time_table[0] - 1

    for i in range(4):
        if flag & (2 ** i):
            tra, index = Que_[i].popleft()
            output_arr[index] = time
            time_table.popleft()

    if (len(Que_[0]) or len(Que_[1]) or len(Que_[2]) or len(Que_[3])):
        pass
    else:
        break

    time += 1

for i in range(N):
    print(output_arr[i])