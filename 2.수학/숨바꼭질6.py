from sys import stdin

# 동생들의 위치에서 수빈이의 위치를 뺀 값들의 최대공약수를 찾자
'''
def find_GCD(a, b):
    r = a % b
    if r == 0:
        return b
    else:
        return find_GCD(b, r)

N, S = map(int, stdin.readline().split()) # N 동생 수, S 수빈의 위치
pos_young = list(map(int, stdin.readline().split()))


for i in range(N):
    pos_young[i] = abs(pos_young[i] - S)

min_val = min(pos_young)

for i in range(N):
    min_val = find_GCD(pos_young[i], min_val)

print(min_val)
'''
def find_GCD(a, b): # lambda 를 이용한
    r = a % b
    if r == 0:
        return b
    else:
        return find_GCD(b, r)

N, S = map(int, stdin.readline().split()) # N 동생 수, S 수빈의 위치

S_list = [S for _ in range(N)]
pos_young = list(map(lambda x, y : abs(int(x) - y), stdin.readline().split(), S_list))

min_val = min(pos_young)

for i in range(N):
    min_val = find_GCD(pos_young[i], min_val)

print(min_val)
