# 시간초과 해결 -> 같은 좌표, 무게값을 가지는 다른 방법일 때 deque 추가하지 않고 무게값을 증가시킴
# 더 이상 진행하지 않아도 되는 좌표, 도착지점일 때 백트래킹

from collections import deque
from sys import stdin

N, K = map(int, stdin.readline().split())
check = [[False, 100000, 0] for _ in range(100001)]

check[N] = [True, 0, 1]

Que = deque()
Que.append((N, 0))

stop_weight = 100000
count = 0

while len(Que):
    cur, weight = Que.popleft()

    if cur == K:
        count = count + check[cur][2]

        if stop_weight == 100000:
            stop_weight = weight

        continue

    if weight > stop_weight:
        break

    if cur < 100000 and cur < K:
        if check[cur + 1][1] >= weight + 1:
            if check[cur + 1][0] is False:
                Que.append((cur + 1, weight + 1))
                check[cur + 1] = [True, weight + 1, check[cur][2]]

            else:
                check[cur + 1][2] += check[cur][2]

    if cur > 0:
        if check[cur - 1][1] >= weight + 1:
            if check[cur - 1][0] is False:
                Que.append((cur - 1, weight + 1))
                check[cur - 1] = [True, weight + 1, check[cur][2]]

            else:
                check[cur - 1][2] += check[cur][2]

    if cur * 2 <= 100000 and cur < K:
        if check[cur * 2][1] >= weight + 1:
            if check[cur * 2][0] is False:
                Que.append((cur * 2, weight + 1))
                check[cur * 2] = [True, weight + 1, check[cur][2]]

            else:
                check[cur * 2][2] += check[cur][2]

print(stop_weight)
print(count)