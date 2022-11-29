from sys import stdin, stdout

N, M = map(int, stdin.readline().split())

output = [0] * M
use = [False] * (N+1)
num_arr = list(map(int, stdin.readline().split()))
num_arr.sort()

def ascend_arr(count, N, M):
    if count == M:
        stdout.write(' '.join(map(str, output)) + '\n')
        return

    for i in range(N):
        if use[i]:
            continue
        for check in range(i+1):
            use[check] = True
        output[count] = num_arr[i]
        ascend_arr(count+1, N, M)
        for check in range(i+1):
            use[check] = False

ascend_arr(0, N, M)
