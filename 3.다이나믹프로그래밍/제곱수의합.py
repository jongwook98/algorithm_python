<<<<<<< HEAD
# 제곱수의 합으로 숫자를 나타낼 때
# 1의 제곱이 있으므로 모든 수를 표현 할 수 있다.
# 1의 제곱이 4개를 2의 제곱 하나로 바꿀 수 있으며
# 2의 제곱 2개와 1의 제곱 하나를 3의 제곱 하나로 바꿀 수 있다.
# 수에 가장 근접한 제곱수를 계속 빼서 계산하면 될 것 같다 -> 다이나믹 프로그래밍 적으로 푸는 것은 아닌듯.
'''
N = int(input())
count = 0

while True:
    count += 1
    sub_num = (int(N ** (1 / 2))**2)
    N -= sub_num
    print(sub_num)
    if N == 0:
        break

print(count)
'''

N = int(input())
D = [0]*(N+1)
for i in range(1, N+1):
    D[i] = i
    j = 1
    while j*j <= i:
        if D[i] > D[i-j*j]+1:
            D[i] = D[i-j*j]+1
        j += 1
=======
# 제곱수의 합으로 숫자를 나타낼 때
# 1의 제곱이 있으므로 모든 수를 표현 할 수 있다.
# 1의 제곱이 4개를 2의 제곱 하나로 바꿀 수 있으며
# 2의 제곱 2개와 1의 제곱 하나를 3의 제곱 하나로 바꿀 수 있다.
# 수에 가장 근접한 제곱수를 계속 빼서 계산하면 될 것 같다 -> 다이나믹 프로그래밍 적으로 푸는 것은 아닌듯.
'''
N = int(input())
count = 0

while True:
    count += 1
    sub_num = (int(N ** (1 / 2))**2)
    N -= sub_num
    print(sub_num)
    if N == 0:
        break

print(count)
'''

N = int(input())
D = [0]*(N+1)
for i in range(1, N+1):
    D[i] = i
    j = 1
    while j*j <= i:
        if D[i] > D[i-j*j]+1:
            D[i] = D[i-j*j]+1
        j += 1
>>>>>>> feb7b03d3ac8b082d54e5e67b97fd44c0252cf76
print(D[N])