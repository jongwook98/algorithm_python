from sys import stdin, stdout

N, M = map(int, stdin.readline().split())

output = [0] * M
pre_num = [0] * M
num_arr = [0] + list(map(int, stdin.readline().split()))
num_arr.sort()

def output_make(count, N, M):
    if count == M:
        stdout.write(' '.join(map(str, output)) + '\n')
        return

    for i in range(1, N+1):
        if pre_num[count] == num_arr[i]:
            continue
        output[count] = num_arr[i]
        pre_num[count] = num_arr[i]
        output_make(count+1, N, M)
    pre_num[count] = 0

output_make(0, N, M)