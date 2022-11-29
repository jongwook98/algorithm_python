'''
from sys import stdin

N = int(stdin.readline()) # 수열의 전체 크기

num_arr = list(map(int, stdin.readline().split()))

portion_arr = [[0] for _ in range(N)] # portion_arr에 들어가는 수는 num_arr 의 인덱스
# 내가 하려는 것은 1000^3 의 알고리즘으로 시간 초과가 무조건 일어날듯,,, 다른방법 생각,
for n in range(N):
    for m in range(0, N):
        if n == 0:
            portion_arr[m].append(m)
        elif num_arr[portion_arr[m][-1]] < num_arr[m]:
            portion_arr[m].append(num_arr[m])

print(portion_arr)
'''
# ********************* 못 풀었음..
# N^3 의 시간복잡도 해결 방법 -> N^2 로 풀 수 있다.
# 모든 수를 넣어서 비교하는 것이 아닌
# 앞에서부터 수를 넣어서 값을 넣어준다
# 그리고 크기가 작은 수가 나타나면 그 배열의 크기를 가져와서 그대로 1 추가함...

from sys import stdin

N = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
D = [0]*N
for n in range(N):
    D[n] = 1
    for m in range(n):
        if arr[m] < arr[n] and D[m]+1 > D[n]:
            D[n] = D[m]+1
print(max(D))
