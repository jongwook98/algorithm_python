'''from sys import stdin # 1차 시도 코드 마지막 테스트 케이스 시간초과:

list pop(index) 의 경우 시간복잡도가 O(N) 이므로 dict 으로 해결해보자

W, N = map(int, stdin.readline().split())
M_arr = []; P_arr = []
result = 0

for i in range(N):
    M, P = map(int, stdin.readline().split())
    M_arr.append(M); P_arr.append(P)

while W > 0:
    pricist = P_arr.index(max(P_arr))
    result += min(W ,M_arr[pricist]) * P_arr[pricist]

    if W > M_arr[pricist]:
        W = W - M_arr[pricist]
        M_arr.pop(pricist); P_arr.pop(pricist)

    else:
        break

print(result)
'''
from sys import stdin # dict 자료형으로 가격이 똑같으면 무게를 추가

#dict pop(key) 의 경우 시간복잡도가 O(1)이다.

W, N = map(int, stdin.readline().split())
metal = dict()
result = 0

for i in range(N):
    M, P = map(int, stdin.readline().split())

    try:
        metal[P] += M
    except:
        metal[P] = M

while W > 0:
    pricist = max(metal.keys())
    result += min(W, metal[pricist]) * pricist

    W = W - metal[pricist]
    metal.pop(pricist)

print(result)