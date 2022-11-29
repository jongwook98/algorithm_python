## 좀 어려운것 같은데,,, 일단 넘어가자.. 다음에 다시 푸는 걸로
# 백트래킹을 구현해야 시간초과가 나지 않는다. 다만 백트래킹으로 인한 시간복잡도 계산은 할 수 없다.
# 얼마나 많은 백트래킹이 이뤄지는지 알 수 없기 때문에..


from sys import stdin

# line 을 기준으로 [0][0] 인덱스를 먼저 예상하고 [0][0] [1][1]의 합인 [0][1]을 확인하여 맞도록 하는 값 찾기

def sign_(sign, sum):
    if sign == '+':
        if sum <= 0:
            return False
    elif sign == '-':
        if sum >= 0:
            return False
    else:
        if sum != 0:
            return False
    return True

def find_num(sign_arr, num_arr, index, sum):
    if index == len(num_arr):
        print(num_arr)
        return num_arr
    for i in range(1, 11):
        for n in range(index+1):
            if not sign_(sign_arr[n][index], sum+num_arr[index]*i):
                continue
            find_num(sign_arr, num_arr, index+1, sum+num_arr[index])

N = int(stdin.readline())
sign = stdin.readline()
sign_arr = [[False] * N for i in range(N)]

count = 0
for i in range(N):
    for j in range(i, N):
        sign_arr[i][j] = sign[count]
        count += 1

num_arr = [False] * N

for i in range(N):
    if sign_arr[i][i] == '+':
        num_arr[i] = 1
    elif sign_arr[i][i] == '-':
        num_arr[i] = -1
    else:
        num_arr[i] = 0

find_num(sign_arr, num_arr, 0, 0)