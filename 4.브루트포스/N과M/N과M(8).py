from sys import stdin, stdout

N, M = map(int, stdin.readline().split())

output = [0] * M
use = [False] * (N+1)
num_arr = list(map(int, stdin.readline().split()))
num_arr.sort()

def output_make(count, N, M):
    if count == M:
        stdout.write(' '.join(map(str, output)) + '\n')
        return

    for i in range(N):
        if use[i]:
            continue
        for check in range(i):
            use[check] = True

        output[count] = num_arr[i]
        output_make(count+1, N, M)

        for check in range(i):
            use[check] = False

output_make(0, N, M)