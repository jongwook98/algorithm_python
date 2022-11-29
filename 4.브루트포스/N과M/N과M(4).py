from sys import stdin, stdout

N, M = map(int, stdin.readline().split())

output = [0] * M
use = [False] * (N+1)

def ascend_arr(count, N, M):
    if count == M:
        stdout.write(' '.join(map(str, output)) + '\n')
        return

    for i in range(1, N+1):
        if use[i]:
            continue
        for under in range(i):
            use[under] = True
        output[count] = i
        ascend_arr(count+1, N, M)
        for under in range(i):
            use[under] = False

ascend_arr(0, N, M)