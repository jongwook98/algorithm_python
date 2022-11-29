from sys import stdin

def prev_permutation(arr):
    i = len(arr)-1
    while i > 0 and arr[i-1] <= arr[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(arr)-1
    while arr[i-1] <= arr[j]:
        j -= 1
    arr[i-1], arr[j] = arr[j], arr[i-1]

    j = len(arr)-1
    while j > i:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return True

def next_permutation(arr):
    i = len(arr)-1
    while i > 0 and arr[i-1] >= arr[i]:
        i -= 1
    if i <= 0:
        return False

    j = len(arr)-1
    while arr[i-1] >= arr[j]:
        j -= 1
    arr[i-1], arr[j] = arr[j], arr[i-1]
    j = len(arr)-1
    while j > i:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return True

def cal_cul(sig, num_arr):
    for i in range(len(sig)):
        if sig[i] == '<':
            if num_arr[i] > num_arr[i+1]:
                return False
        else:
            if num_arr[i] < num_arr[i+1]:
                return False
    return True

N = int(stdin.readline())
sig_arr = list(stdin.readline().split())
max_num = [i for i in range(9, 9-(N+1), -1)]
min_num = [i for i in range(N+1)]

while True:
    if cal_cul(sig_arr, max_num):
        print(''.join(map(str, max_num)))
        break
    if not prev_permutation(max_num):
        break

while True:
    if cal_cul(sig_arr, min_num):
        print(''.join(map(str, min_num)))
        break
    if not next_permutation(min_num):
        break