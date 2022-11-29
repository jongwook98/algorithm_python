from sys import stdin, stdout

N, M = map(int, stdin.readline().split())

output = [0] * M
pre_num = [0] * M

use = [False] * (N+1)
num_arr = [0] + list(map(int, stdin.readline().split()))
num_arr.sort()

def output_make(count, N, M):
    if count == M:
        stdout.write(' '.join(map(str, output)) + '\n')
        return

    for i in range(1, N+1):
        if use[i] or pre_num[count] == num_arr[i]:
            continue
        for check in range(i+1):
            use[check] = True
        output[count] = num_arr[i]
        pre_num[count] = num_arr[i]
        output_make(count+1, N, M)

        for check in range(i+1):
            use[check] = False
    pre_num[count] = 0 # for 문을 다 돌고나서 중복 사용 체크 부분 초기화

output_make(0, N, M)