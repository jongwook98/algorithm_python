from sys import stdin

factorial_num = int(stdin.readline())
num = 1

for i in range(1, factorial_num+1):
    num *= i

print(num)