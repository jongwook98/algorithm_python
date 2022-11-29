# 통과는 했지만 시간을 더 줄일 수 있는 방법들을 생각해보면
# 내구도가 0인 구간을 계속 계산하기보다 0이 되는 순간에 count 시키면 될 것 같다.

from sys import stdin
from collections import deque

N, K = map(int, stdin.readline().split())
dur = deque(list(map(int, stdin.readline().split())))

robot_placed = []
step = 0

pop_list = []

while True:
    step += 1
    dur.appendleft(dur.pop())
    for i in range(len(robot_placed)):
        robot_placed[i] += 1
        if robot_placed[i] == (N-1):
            pop_list.append(i)

    pop_list.sort(reverse=True)
    for i in pop_list:
        robot_placed.pop(i)

    pop_list = []

    for i in range(len(robot_placed)):
        if robot_placed[i] + 1 >= (2*N):
            if dur[0] != 0 and 0 not in robot_placed:
                robot_placed[i] = 0
                dur[0] -= 1

        else:
            if dur[robot_placed[i] + 1] != 0 and (robot_placed[i] + 1) not in robot_placed:
                robot_placed[i] += 1
                dur[robot_placed[i]] -= 1
            if robot_placed[i] == (N-1):
                pop_list.append(i)

    pop_list.sort(reverse=True)
    for i in pop_list:
        robot_placed.pop(i)

    pop_list = []

    if dur[0] != 0:
        robot_placed.append(0)
        dur[0] -= 1

    if dur.count(0) >= K:
        break

print(step)