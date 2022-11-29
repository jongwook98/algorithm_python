# 카드구매하기 1 과 같이 다이나믹 프로그래밍 알고리즘으로 작성한다음
# max -> min 으로 바꿔주면 될 것 같은데?

# 카드 구매가 4장이었을 때
# 한장을 구매하는 가장 저렴한 방법 + 3장 구매
# 두장을 구매하는 가장 저렴한 방법 + 2장 구매
# 세장을 구매하는 가장 저렴한 방법 + 1장 구매
# 네장을 구매하는 가장 저렴한 방법 + 0장 구매?
# pay[0] 은 0이 맞고,

from sys import stdin

N = int(stdin.readline())
price_ = [0] + list(map(int, stdin.readline().split()))
pay_ = [0] + [False] * (N)

for i in range(1, N+1):
    for f in range(1, i+1):
        if pay_[i] == False:
            pay_[i] = pay_[i - f] + price_[f]
        pay_[i] = min(pay_[i], pay_[i-f] + price_[f])

print(pay_[N])