from sys import stdin

Num = int(stdin.readline().strip())
inf = int(1e5)

DP = [inf for _ in range(Num + 1)]
DP[Num] = 0

i = len(DP) - 1
while i > 0:
    if i % 5 == 0:
        DP[i // 5] = min(DP[i // 5], DP[i] + 1)

    if i % 3 == 0:
        DP[i // 3] = min(DP[i // 3], DP[i] + 1)

    if i % 2 == 0:
        DP[i // 2] = min(DP[i // 2], DP[i] + 1)

    DP[i - 1] = min(DP[i - 1], DP[i] + 1)
    i -= 1

print(DP[1])
