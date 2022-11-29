# 다이나믹프로그래밍
# 점화식 세워서 하기,

N = int(input())

check = [-1] * (5000+1)
check[3] = 1
check[5] = 1

for i in range(3, N+1):
    if check[i-5] != -1:
        check[i] = check[i-5] + 1

    elif check[i-3] != -1:
        check[i] = check[i-3] + 1

print(check[N])