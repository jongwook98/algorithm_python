from sys import stdin

N, K = map(int, stdin.readline().split())

S = list(map(int, stdin.readline().split()))

for _ in range(K):
    A, B = map(int, stdin.readline().split())
    sum_score = 0

    for i in range(A - 1, B):
        sum_score += S[i]

    print(sum_score / (B - A + 1))
