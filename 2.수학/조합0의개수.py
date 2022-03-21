from sys import stdin

N, M = map(int, stdin.readline().strip().split())

num_of_plus_zero = 0
num_of_minus_zero = 0

for i in range(N+1, 5):
    num = i

    if num % 5 == 0:
        if i <= M:
            num_of_minus_zero += 1
        if i <= (N-M):
            num_of_minus_zero += 1
        num_of_plus_zero += 1
        num /= 5

print(num_of_plus_zero - num_of_minus_zero)