from sys import stdin
#from math import sqrt

def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

M, N = map(int, input().split())

for i in range(M, N+1):
    if isPrime(i):
        print(i)

'''
# 백준 알고리즘에 올라온 런타임 1/10 python3 코드
import sys

M, N = 0, 0
DB = []

def solution():
    for base in range(2, N+1):
        if not DB[base]: continue
        for i in range(base*2, N+1, base): DB[i] = 0
    return filter(lambda x: DB[x], range(M, N+1))

# driver
input = sys.stdin.readline
M, N = map(int, input().split())
DB, DB[1] = [1] * (N+1), 0
print('\n'.join(map(str, solution())))
'''

'''# 시간 초과.. 내가 구현한 방식 : 최소값에서 최대값까지 리스트 만들어서 소수가 아닌 숫자 제거
def prime(min, max):
    prime_array = [i for i in range(min, max+1)]

    for i in range(2, int(max**0.5)+1):
        for q in range(i, int(max/i) + 1):
            try:
                prime_array.remove(i*q)
            except:
                pass

    return prime_array

def main():
    M, N = map(int, stdin.readline().split())
    prime_array = prime(M, N)

    for i in range(len(prime_array)):
        if prime_array[i] >= M:
            print(prime_array[i])

if __name__ == "__main__":
    main()
'''