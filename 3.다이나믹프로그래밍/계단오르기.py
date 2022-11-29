# 점화식, 규칙 마지막 계단은 밟아야함, 계단을 밟는 규칙이 있음. 한 칸 count + 1, 두 칸 count 초기화

# 해당 계단에 도착해서 count가 0일 때, 1일 때, 2일 때 큰 수를 저장하자!

from sys import stdin

N = int(stdin.readline().strip())
step = [[0] for _ in range(N+1)]
check = [[[0, 0], [0, 0]] for _ in range(N+1)]

for i in range(1, N+1):
    step[i] = int(stdin.readline().strip())

check[0][0] = [0, 0]
check[0][1] = [False, False]

check[1][0] = [step[1], 0]
check[1][1] = [False, False]

for i in range(2, N+1):
    check[i][0] = [max(check[i-2][0][0], check[i-2][1][0]) + step[i], 0]

    if check[i-1][0][0]:
        check[i][1] = [check[i-1][0][0] + step[i], 1]

print(max(check[N][0][0], check[N][1][0]))