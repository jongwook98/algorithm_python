# 최대공약수 구하는 공식 - 유클리드 호제법
# GCD(a, b) = GCD(b, r)
# 반복해서 r = 0 이 되면 그때의 b 가 최대공약수
# 최소공배수는 최대공약수와의 곱이 A * B 가 같음을 이용한다.
from sys import stdin

A, B = map(int, stdin.readline().split())
a = A; b = B

if B > A:
    temp = A
    A = B; B = temp

while True:
    r = a % b
    a = b; b = r
    if r == 0:
        print(a)
        break

print(round(A*B/a))