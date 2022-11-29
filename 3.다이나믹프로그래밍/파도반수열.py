from sys import stdin

T = int(stdin.readline().strip())
for _ in range(T):
    N = int(stdin.readline().strip())
    DP = [0 for _ in range(N)]

    DP[0] = 1

    if N > 1:
        DP[1] = 1

    if N > 2:
        DP[2] = 1
        for index in range(3, N):
            DP[index] = DP[index - 2] + DP[index - 3]

    print(DP[N - 1])