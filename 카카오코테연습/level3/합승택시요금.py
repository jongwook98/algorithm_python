def solution(n, s, a, b, fares):

    INF = int(1e9)

    graph = []
    DP = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

    total = [INF for _ in range(n + 1)]

    for c, d, f in fares:
        graph.append((c, d, f))

    for c, d, f in graph:
        DP[c][d] = f
        DP[d][c] = f

    for index in range(n + 1):
        DP[index][index] = 0

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                DP[i][j] = min(DP[i][j], DP[i][k] + DP[k][j])

    for i in range(1, n + 1):
        total[i] = DP[s][i] + DP[i][a] + DP[i][b]

    return min(total)