# 순열 풀던 방식으로 풀었다..
from sys import stdin

def next_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i-1] <= a[i]:
        i -= 1
    if i <= 0:
        return False

    j = len(a) - 1
    while a[j] >= a[i-1]:
        j -= 1

    a[i-1], a[j] = a[j], a[i-1]
    j = len(a) - 1
    while j > i:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    return True

L, C = map(int, stdin.readline().split())
alpha = list(stdin.readline().split())
alpha.sort()

select_arr = [1] * L + [0] * (C-L)

while True:
    count = 0
    for i in range(C):
        if select_arr[i]:
            if alpha[i] in ['a', 'e', 'i', 'o', 'u']:
                count += 1
    if count == 0 or L - count < 2:
        if not next_permutation(select_arr):
            break
        continue

    else:
        for i in range(C):
            if select_arr[i]:
                print(alpha[i], end='')
        print()

    if not next_permutation(select_arr):
        break
