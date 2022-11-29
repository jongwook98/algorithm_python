# 2xn 타일링 문제에서 2x2 사각형 하나만 추가 됬으므로
# 다이나믹 프로그래밍 식은 D[n] = D[n-1] + 2D[n-2] 일 것 같은데??

num_of_method = [0 for _ in range(1001)]

N = int(input())
num_of_method[1] = 1
num_of_method[2] = 3

if N >= 3:
    for i in range(3, N+1):
        num_of_method[i] = (num_of_method[i-1] + 2*num_of_method[i-2]) % 10007

print(num_of_method[N])
