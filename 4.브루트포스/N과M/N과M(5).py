from sys import stdin, stdout

N, M = map(int, stdin.readline().split())

output = [0] * M
use = [False] * (N+1)

num_arr = [0] + list(map(int, stdin.readline().split()))
num_arr.sort()

def ascend_arr(count, N, M):
    if count == M:
        stdout.write(' '.join(map(str, output)) + "\n")
        return

    for i in range(1, len(num_arr)):
        if use[i]:
            continue
        output[count] = num_arr[i]
        use[i] = True
        ascend_arr(count+1, N, M)
        use[i] = False

ascend_arr(0, N, M)