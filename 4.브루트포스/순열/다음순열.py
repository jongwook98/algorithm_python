# 2 4 5 3 1 # 2 5 1 3 4

# next_permutation
# step 1 : 뒤에서부터 오름차순이 아닌 것 찾기
# step 2 : 오름차순이 끊기는 숫자와, 끝에서 부터 그 숫자 보다 큰 숫자 찾기
# step 3 : 두 숫자를 swap
# step 4 : 바뀐 숫자 뒤 부터 오름차순으로 정렬하기

def next_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i-1] >= a[i]: # step 1
        i -= 1
    if i <= 0: # a 배열이 전부 오름차순 일 때
        return False
    j = len(a) - 1
    while a[j] <= a[i-1]: # step 2 오름차순이 끊기는 숫자 index = i
        j -= 1

    a[i-1], a[j] = a[j], a[i-1] # step 3 두 숫자를 swap

    j = len(a) - 1
    while i < j: # step 4
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    return True # 다음 순열을 정상적으로 구했음을 알림

n = int(input())
a = list(map(int, input().split()))

if next_permutation(a):
    print(' '.join(map(str, a)))
else:
    print(-1)

'''
from sys import stdin, stdout

N = int(stdin.readline())

num_arr = list(map(int, stdin.readline().split()))
pre_num = 0

def find_next(arr):
    for i in range(-2, -len(num_arr) - 1, -1):
        if num_arr[i + 1] > num_arr[i]: # 감소순열이 아닌 부분 찾기
            for t in range(-1, i, -1):
                if num_arr[i] < num_arr[t]:
                    temp = num_arr[i]
                    num_arr[i] = num_arr[t]
                    num_arr[t] = temp

                    new_arr = num_arr[i+1:]
                    for a in range(-1, i, -1):
                        num_arr[a] = new_arr[-(a+1)]

                    stdout.write(' '.join(map(str, num_arr)))
                    return

    return print('-1')

find_next(num_arr)
'''