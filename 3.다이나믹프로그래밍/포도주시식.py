# 12 ������ check[i-1][0]�� �߰� �ؾ߸� �� ���� -> �� �� �̻����� �ǳʶ� �� �ֵ��� ����

from sys import stdin

N = int(stdin.readline())
wine = [int(stdin.readline()) for _ in range(N)]

check = [[0 for _ in range(3)] for _ in range(N)]
check[0][1] = wine[0]

for i in range(1, N):
    check[i][0] = max(check[i-1][0], check[i-1][1], check[i-1][2])
    check[i][1] = check[i-1][0] + wine[i]
    check[i][2] = check[i-1][1] + wine[i]

print(max(check[N-1]))