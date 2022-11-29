from sys import stdin

N, M = map(int, stdin.readline().split())

use = [False] * (N)
output = [0 for _ in range(M)]

def ascend_arr(count, N, M):
    if count == M:
        for m in range(M):
            print(output[m] ,end = ' ')
        print()

        return
    for i in range(1, N+1):
        if use[i-1]:
            continue
        output[count] = i
        use[i-1] = True
        ascend_arr(count+1, N, M)
        use[i-1] = False

ascend_arr(0, N, M)


'''
import sys
n,m = map(int,input().split())
c = [False]*(n+1)
a = [0]*m

def go(index, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str,a))+'\n')
        return
    for i in range(1, n+1):
        if c[i]:
            continue
        c[i] = True
        a[index] = i
        go(index+1, n, m)
        c[i] = False

go(0,n,m)
'''
# 0 4 4
# 1234
# 123