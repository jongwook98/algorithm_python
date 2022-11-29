def next_permutation(a):
    i = len(a)-1
    while i >= 0 and a[i-1] <= a[i]:
        i -= 1
    if i <= 0:
        return False

    j = len(a)-1
    while a[i-1] >= a[j]:
        j -= 1

    a[i-1], a[j] = a[j], a[i-1]

    j = len(a)-1
    while j > i:
        a[i], a[j] = a[j], a[i]
        j -= 1
        i += 1
    return True

n = int(input())
a = list(map(int, input().split()))
while True:
    print(' '.join(map(str, a)) + '\n')
    if not next_permutation(a):
        break

'''
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
'''