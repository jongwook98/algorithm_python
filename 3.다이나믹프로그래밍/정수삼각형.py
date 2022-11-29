from sys import stdin

N = int(stdin.readline().strip())

num_arr = [[False] for _ in range(N)]
check = [[False] * N for _ in range(N)]

for i in range(N):
    num_arr[i] = list(map(int, stdin.readline().split()))

check[0][0] = num_arr[0][0]

for i in range(1, N):
    for j in range(i+1):
        if j == 0:
            check[i][j] = check[i-1][j] + num_arr[i][j]
        elif j == i:
            check[i][j] = check[i-1][j-1] + num_arr[i][j]
        else:
            check[i][j] = max(check[i-1][j-1], check[i-1][j]) + num_arr[i][j]

print(max(check[N-1]))