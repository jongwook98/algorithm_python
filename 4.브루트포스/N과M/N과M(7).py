from sys import stdin, stdout

N, M = map(int, stdin.readline().split())

output = [0] * M
num_arr = list(map(int, stdin.readline().split()))
num_arr.sort()

def output_make(count, N, M):
    if count == M:
        stdout.write(' '.join(map(str, output)) + '\n')
        return

    for i in range(N):
        output[count] = num_arr[i]
        output_make(count+1, N, M)

output_make(0, N, M)