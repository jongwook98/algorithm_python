from sys import stdin

T = int(stdin.readline().strip())

for _ in range(T):
    MAX_ = 0

    N = int(stdin.readline().strip())
    DP = [[0 for _ in range(N)] for _ in range(2)]

    sticker = [(list(map(int, stdin.readline().split()))) for _ in range(2)]

    DP[0][0] = sticker[0][0]
    DP[1][0] = sticker[1][0]

    MAX_ = max(DP[0][0], DP[1][0])

    if N > 1:
        DP[0][1] = max(DP[1][0] + sticker[0][1], DP[0][0])
        DP[1][1] = max(DP[0][0] + sticker[1][1], DP[1][0])

        MAX_ = max(DP[0][1], DP[1][1])

        for index in range(2, N):
            for line in range(2):
                DP[line][index] = max(DP[1 - line][index - 1] + sticker[line][index], DP[line][index - 2] + sticker[line][index], DP[line][index - 1])
                MAX_ = max(MAX_, DP[line][index])
    print(MAX_)