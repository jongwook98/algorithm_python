from sys import stdin, stdout

N, M = map(int, stdin.readline().split())

output = [0] * M

def ascend_arr(count, N, M):
    if count == M:
        stdout.write(' '.join(map(str, output)) + '\n')
        return

    for i in range(1, N+1):
        output[count] = i
        ascend_arr(count+1, N, M)

ascend_arr(0, N, M)