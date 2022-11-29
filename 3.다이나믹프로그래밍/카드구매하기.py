# 생각의 흐름
# 개당 가격을 구한 다음,
# 예 1 1, 2 10 3 16   4 4
#    1 1  2 5  3 5.3  4 1 이런 경우의 반례가 발생

# 생각하지 못한 알고리즘.... 다이나믹 프로그래밍으로 생각한다면
# D[i] = D[i-f] + P[f] 란다.. 그 중 가장 큰 것을 선택

from sys import stdin

N = int(stdin.readline())
price_arr = [0] + list(map(int, stdin.readline().split())) ##### 자꾸 틀렸던 이유,, 카드 0개를 사는 비용인 0원을 추가하지 않았음.
                                    # 위 표현으로 0번째 인덱스에 0을 추가할 수 있다..
pay_price = [0 for _ in range(N+1)] # 다른 표현 [0] * n+1

for i in range(1, N+1):
    for f in range(1, i+1):
        pay_price[i] = max(pay_price[i], pay_price[i-f] + price_arr[f])

print(pay_price[N])