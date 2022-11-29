# list의 요소가 있는지 없는지 확인하는 in 의 시간 복잡도는 O(N) 이다.
# 이분 탐색을 구현한다면 그것의 시간 복잡도는 O(logN) 이다.
# set, dictionary 자료구조를 이용하면 요소가 있는지 없는지 확인하는 시간 복잡도는 O(1) 이다.

#0. set 자료구조 이용 걸리는 시간 약 156 ms

from sys import stdin, stdout
N = stdin.readline()
arr_A = set(stdin.readline().split())
M = stdin.readline()
arr_B = stdin.readline().split()

for l in arr_B:
    stdout.write('1\n') if l in arr_A else stdout.write('0\n')

'''
#1. 이분 탐색 걸리는 시간 약 712 ms
from sys import stdin

N = int(stdin.readline().strip())
arr_A = sorted(map(int, stdin.readline().split()))

M = int(stdin.readline().strip())
arr_B = map(int, stdin.readline().split())

def binary(l, arr_A, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if l == arr_A[m]:
        return 1
    elif l < arr_A[m]:
        return binary(l, arr_A, start, m-1)
    else:
        return binary(l, arr_A, m+1, end)

for l in arr_B:
    start = 0
    end = len(arr_A) - 1
    print(binary(l, arr_A, start, end))
'''

'''
시간 초과 코드

from sys import stdin

N = int(stdin.readline().strip())
arr_A = list(map(int, stdin.readline().split()))

M = int(stdin.readline().strip())
arr_B = list(map(int, stdin.readline().split()))

for i in arr_B:
    try:
        if arr_A.index(i):
            print(1)
    except:
        print(0)
'''