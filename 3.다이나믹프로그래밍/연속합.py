'''
from sys import stdin # 시간 초과

N = int(stdin.readline())

sum_N = [0 for _ in range(N)] # sum_N[n] 은 ? ~ n 까지의 합 중 가장 큰 수

num_arr = list(map(int, stdin.readline().split()))

for n in range(N):
    sum_N[n] = num_arr[n]
    for m in range(n): -> 이 구조 왜 사용했지?? 전혀 쓰지 않고 있다.
        sum_N[n] = max(num_arr[n], sum_N[n-1] + num_arr[n])

print(max(sum_N))
'''
from sys import stdin

N = int(stdin.readline())

sum_N = [0 for _ in range(N)] # sum_N[n] 은 ? ~ n 까지의 합 중 가장 큰 수

num_arr = list(map(int, stdin.readline().split()))

for n in range(N):
    sum_N[n] = max(num_arr[n], sum_N[n-1] + num_arr[n])

print(max(sum_N))