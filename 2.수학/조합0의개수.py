from sys import stdin

# 구현은 성공했으나 시간초과....
# 핵심은 2와 5의 소인수를 구하는 알고리즘의 시간을 줄이는 방법인듯
# python 의 // 연산은 소수 부분은 버리고 정수 부분만 추출

N, M = map(int, stdin.readline().strip().split())

def two_count(n):
    two = 0
    while n != 0:
        n = n // 2
        two += n
    return two

def five_count(n):
    five = 0
    while n != 0:
        n = n // 5
        five += n
    return five


num_of_two = two_count(N) - two_count(M) - two_count(N-M)
num_of_five = five_count(N) - five_count(M) - five_count(N-M)

print(min(num_of_two, num_of_five))
''' 내 알고리즘...
N, M = map(int, stdin.readline().strip().split())

num_of_two = 0
num_of_five = 0

for i in range(1, N+1):
    count = 1
    if i <= M:
        count -= 1
    if i <= (N-M):
        count -= 1

    num = i
    while num != 0:
        num_of_two += count
        num = num // 2

    num = i
    while num != 0:
        num_of_five += count
        num = num // 5

print(min(num_of_two, num_of_five))
'''