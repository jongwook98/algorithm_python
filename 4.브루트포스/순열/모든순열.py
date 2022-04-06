from sys import stdin, stdout

N = int(stdin.readline())
output = [0] * N
use = [False] * (N+1)

def find_arr(count, N):
    if count == N:
        stdout.write(' '.join(map(str, output)) + '\n')
        return

    for i in range(1, N+1):
        if use[i]:
            continue

        output[count] = i
        use[i] = True
        find_arr(count+1, N)
        use[i] = False

find_arr(0, N)