# 인접한 수?
# 1 2 3 4 5 6 7 8 9 N 이 1 일 때 인접한 수는 9개고
# 12 23 34 45 56 67 78 89 98 87 76 65 54 43 32 21 10 이렇게 17개 인듯

# 9나 0으로 끝나는 경우는 다음 이동 가능 수가 하나임

stare_num = [[0]*10 for _ in range(101)] # python [101][4] 배열 생성 -> 각 숫자로 끝나는 모든수를 기억하는게 편할 듯 하다.

for n in range(1, 101):
    for m in range(0, 10):
        if n == 1:
            if m == 0:
                stare_num[n][m] = 0
            else:
                stare_num[n][m] = 1
        elif m == 0:
            stare_num[n][m] = stare_num[n-1][m+1] % 1000000000
        elif m == 9:
            stare_num[n][m] = stare_num[n-1][m-1] % 1000000000
        else:
            stare_num[n][m] = (stare_num[n-1][m-1] + stare_num[n-1][m+1]) % 1000000000

N = int(input())
print(sum(stare_num[N]) % 1000000000)