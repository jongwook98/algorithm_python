from collections import defaultdict
from sys import stdin

INF = int(1e5)

N, M = map(int, stdin. readline().split())
graph = defaultdict(set)

DP = [[INF for _ in range(N + 1)] for _ in range(N + 1)]

for index in range(1, N + 1):
    DP[index][index] = 0

for _ in range(M):
    A, B = map(int, stdin.readline().split())
    graph[A].add(B)
    graph[B].add(A)

X, K = map(int, stdin.readline().split())

for i in range(1, N + 1):
    for j in graph[i]:
        DP[i][j] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            DP[i][j] = min(DP[i][j], DP[i][k] + DP[k][j])

if DP[1][K] == INF or DP[K][X] == INF:
    print(-1)
else:
    print(DP[1][K] + DP[K][X])

"""
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
"""