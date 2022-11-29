def prev_permutation(a):
    i = len(a)-1
    while i > 0 and a[i-1] <= a[i]:
        i -= 1
    if i <= 0:
        return False

    j = len(a)-1
    while a[i-1] >= a[j]:
        j -= 1

    a[i-1], a[j] = a[j], a[i-1]
    j = len(a)-1

    while j >= (i-1):
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    return True

n = int(input())
a = list(map(int, input().split()))
if prev_permutation(a):
    print(' '.join(map(str, a)))
else:
    print(-1)

'''
from sys import stdin, stdout

N = int(stdin.readline())

num_arr = list(map(int, stdin.readline().split()))

# 2 4 5 3 1 -> 2 4 5 1 3
# 2 5 1 3 4 -> 2 4 5 3 1

def find_pre():
    for i in range(-2, -len(num_arr)-1, -1):
        if num_arr[i] > num_arr[i+1]:
            for t in range(-1, i, -1):
                if num_arr[i] > num_arr[t]:
                    temp = num_arr[i]
                    num_arr[i] = num_arr[t]
                    num_arr[t] = temp
                    new_arr = num_arr[:]
                    for a in range(-1, i, -1):
                        num_arr[a] = new_arr[i-a]

                    stdout.write(' '.join(map(str, num_arr)))
                    return
    return print('-1')

find_pre()
'''