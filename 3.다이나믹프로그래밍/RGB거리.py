# 각각의 색깔로 끝나는 최저 비용을 계속 가져가면 되지 않을까
from sys import stdin

N = int(stdin.readline().strip())
cost = [[0, 0, 0] for _ in range(N+1)]
pay_min = [[0, 0, 0] for _ in range(N+1)]

for i in range(1, N+1):
    cost[i] = list(map(int, stdin.readline().split()))

for i in range(1, N+1):
    pay_min[i][0] = min(pay_min[i - 1][2] + cost[i][0], pay_min[i - 1][1] + cost[i][0])
    pay_min[i][1] = min(pay_min[i - 1][2] + cost[i][1], pay_min[i - 1][0] + cost[i][1])
    pay_min[i][2] = min(pay_min[i - 1][1] + cost[i][2], pay_min[i - 1][0] + cost[i][2])

=======
# 각각의 색깔로 끝나는 최저 비용을 계속 가져가면 되지 않을까
from sys import stdin

N = int(stdin.readline().strip())
cost = [[0, 0, 0] for _ in range(N+1)]
pay_min = [[0, 0, 0] for _ in range(N+1)]

for i in range(1, N+1):
    cost[i] = list(map(int, stdin.readline().split()))

for i in range(1, N+1):
    pay_min[i][0] = min(pay_min[i - 1][2] + cost[i][0], pay_min[i - 1][1] + cost[i][0])
    pay_min[i][1] = min(pay_min[i - 1][2] + cost[i][1], pay_min[i - 1][0] + cost[i][1])
    pay_min[i][2] = min(pay_min[i - 1][1] + cost[i][2], pay_min[i - 1][0] + cost[i][2])

print(min(pay_min[N]))