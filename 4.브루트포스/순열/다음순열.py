# 2 4 5 3 1 # 2 5 1 3 4

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
