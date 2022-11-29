from sys import stdin

# 배낭문제 점화식을 세울 수 없어서 인터넷으로 찾아봤다..

# 배낭문제는 많이 유명한 것 같고
# 물건이 하나일 때 가정한다면

# 이 점화식은 물론 index 가 범위를 만족할 때 적용
# DP[i][j] = max(DP[i - 1][j], DP[i - 1][j - W[i]] + V[i]);

# 물건 : i
# 배낭 무게 : j
# 물건 무게 : W
# 물건 가치 : V

N, K = map(int, stdin.readline().split())
items = [list(map(int, stdin.readline().split())) for _ in range(N)]

DP = [[0 for _ in range(K + 1)] for _ in range(N)]

for j in range(K+1):
    for i in range(N):
        if i == 0:
            if j >= items[i][0]:
                DP[i][j] = items[i][1]
        else:
            if j - items [i][0] >= 0:
                DP[i][j] = max(DP[i-1][j], DP[i-1][j - items[i][0]] + items[i][1])
            else:
                DP[i][j] = DP[i-1][j]

print(DP[N-1][K])