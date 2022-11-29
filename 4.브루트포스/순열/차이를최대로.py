#### 못 품,,###

# 10! 까지 1초 안에서 해결 가능
# N 개의 범위를 생각해봤을 때 8 까지의 입력이므로 팩토리얼을 이용해야하는지 생각해보자

# N 개의 순서를 변경해서 만드는 모든 순열은 N X N! 이므로 1초 이내에 가능하다

# 모든 경우를 다 해보는 경우

from sys import stdin

N = int(stdin.readline())
num_arr = list(map(int, stdin.readline().split()))
output = [0] * N
use = [False] * N

max_sub_ = 0
max_arr = []

def calcu(arr):
    sum_ = 0
    for i in range(N-1):
        sum_ += abs(arr[i] - arr[i+1])

    return sum_

def make_numarr(count, N):
    global max_arr

    if count == N:
        max_arr.append(calcu(output))
        return

    for i in range(N):
        if use[i]:
            continue

        output[count] = num_arr[i]
        use[i] = True
        make_numarr(count+1, N)
        use[i] = False

make_numarr(0, N)
print(max(max_arr))