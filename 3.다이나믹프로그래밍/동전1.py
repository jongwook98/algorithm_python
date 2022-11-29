from sys import stdin

N, K = map(int, stdin.readline().split())
DP = [0 for _ in range(K + 1)]

coin = [int(stdin.readline().strip()) for _ in range(N)]

for worth in range(len(coin)):

    # 코인 하나의 가치가 K 가 넘어가면 스킵
    if coin[worth] > K:
        continue

    # 코인 하나로 가치를 나타낼 수 있으면 가지수 추가
    DP[coin[worth]] += 1

    for index in range(K + 1):
        if index >= coin[worth]:
            # DP[index - coin[worth]] + coin[worth]로 하나 추가가
           DP[index] += DP[index - coin[worth]]

print(DP[K])