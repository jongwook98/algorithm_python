from sys import stdin

K, P, N = map(int, stdin.readline().split())
# 식 k * P^N % 1000000007
print(K*pow(P, N, 1000000007)%1000000007,end='') # pow 의 매개변수 3개 3번째 인자 모듈러 연산 - pow(2, 4, 3) => 2의 4승 3으로 나눈 나머지 출력