from sys import stdin

N, M = map(int, stdin.readline().split())
num_arr = [[0] * M] * N
max_val = 0

for n in range(N):
    num_arr[n] = list(map(int, stdin.readline().split()))

for n in range(N):
    for m in range(M): # n,m 은 테트로미노의 시작점

        if m+3 < M:
            max_val = max(max_val, sum(num_arr[n][m:m+4]))
        if n+3 < N:
            sum_val = num_arr[n][m] + num_arr[n+1][m] + num_arr[n+2][m] + num_arr[n+3][m]
            max_val = max(max_val, sum_val)
        if m+2 < M and n+1 < N:
            sum_val = sum(num_arr[n][m:m+3]) + num_arr[n+1][m+2]
            max_val = max(max_val, sum_val)
        if m+2 < M and n-1 >= 0:
            sum_val = sum(num_arr[n][m:m+3]) + num_arr[n-1][m+2]
            max_val = max(max_val, sum_val)
        if m+2 < M and n+1 < N:
            sum_val = sum(num_arr[n][m:m+3]) + num_arr[n+1][m+1]
            max_val = max(max_val, sum_val)
        if m+2 < M and n-1 >= 0:
            sum_val = sum(num_arr[n][m:m+3]) + num_arr[n-1][m+1]
            max_val = max(max_val, sum_val)
        if m+2 < M and n+1 < N:
            sum_val = sum(num_arr[n][m:m+3]) + num_arr[n+1][m]
            max_val = max(max_val, sum_val)
        if m+2 < M and n-1 >= 0:
            sum_val = sum(num_arr[n][m:m+3]) + num_arr[n-1][m]
            max_val = max(max_val, sum_val)
        if m+1 < M and n+2 < N:
            sum_val = sum(num_arr[n][m:m+2]) + num_arr[n+1][m+1] + num_arr[n+2][m+1]
            max_val = max(max_val, sum_val)
        if m+1 < M and n+2 < N:
            sum_val = sum(num_arr[n][m:m+2]) + num_arr[n+1][m] + num_arr[n+2][m]
            max_val = max(max_val, sum_val)
        if m+1 < M and n+2 < N:
            sum_val = sum(num_arr[n+2][m:m+2]) + num_arr[n][m] + num_arr[n+1][m]
            max_val = max(max_val, sum_val)
        if m+1 < M and n-2 >= 0:
            sum_val = sum(num_arr[n][m:m+2]) + num_arr[n-1][m+1] + num_arr[n-2][m+1]
            max_val = max(max_val, sum_val)
        if m+1 < M and n+2 < N:
            sum_val = sum(num_arr[n+1][m:m+2]) + num_arr[n][m] + num_arr[n+2][m]
            max_val = max(max_val, sum_val)
        if m+1 < M and n-1 >= 0 and n+1 < N:
            sum_val = sum(num_arr[n][m:m+2]) + num_arr[n-1][m+1] + num_arr[n+1][m+1]
            max_val = max(max_val, sum_val)
        if m+2 < M and n-1 >= 0:
            sum_val = sum(num_arr[n][m:m+2]) + sum(num_arr[n-1][m+1:m+3])
            max_val = max(max_val, sum_val)
        if m+2 < M and n+1 < N:
            sum_val = sum(num_arr[n][m:m+2]) + sum(num_arr[n+1][m+1:m+3])
            max_val = max(max_val, sum_val)
        if m+1 < M and n-2 >= 0:
            sum_val = sum(num_arr[n-1][m:m+2]) + num_arr[n][m] + num_arr[n-2][m+1]
            max_val = max(max_val, sum_val)
        if m+1 < M and n+2 < N:
            sum_val = sum(num_arr[n+1][m:m+2]) + num_arr[n][m] + num_arr[n+2][m+1]
            max_val = max(max_val, sum_val)
        if m+1 < M and n+1 < N:
            sum_val = sum(num_arr[n][m:m+2]) + sum(num_arr[n+1][m:m+2])
            max_val = max(max_val, sum_val)

print(max_val)