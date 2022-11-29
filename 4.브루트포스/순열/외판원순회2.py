# 입력 N의 범위가 10 이하이므로 팩토리얼 까지 가능 -> 10 이므로 10 X 10! 는 약 3.5 초가 넘어감
# 시간초과

# 알고리즘 에러 - 마지막 route 에서 0으로 갈 수 없는 길일 때 못가도록 해야함
# 알고리즘 에러 - 갈 수 없는 길에 대한 처리가 미흡했다.

def next_permutation(a):
    i = len(a)-1
    while i >= 1 and a[i-1] >= a[i]:
        i -= 1
    if i <= 1:
        return False

    j = len(a)-1
    while a[i-1] >= a[j]:
        j -= 1

    a[i-1], a[j] = a[j], a[i-1]

    j = len(a)-1
    while j > i:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True

def cal_cul(a, price_arr):
    start = a[0]
    dep = a[0]
    sum_pay = 0
    for i in range(1, len(a)):
        if price_arr[dep][a[i]] == 0:
            return 1000000000
        sum_pay += price_arr[dep][a[i]]
        dep = a[i]

    if price_arr[dep][start] == 0:
        return 100000000
    sum_pay += price_arr[a[i]][start]
    return sum_pay

N = int(input())
price_arr = [0] * N
route = [i for i in range(N)]
min_pay = 10000000000
for i in range(N):
    price_arr[i] = list(map(int, input().split()))

while True:
    min_pay = min(min_pay, cal_cul(route, price_arr))
    #print(route)
    if not next_permutation(route):
        break

print(min_pay)


'''
from sys import stdin

N = int(stdin.readline())

payment_arr = [0] * N

for i in range(N):
    payment_arr[i] = list(map(int, stdin.readline().split()))

# 한 번 갔던 도시는 갈 수 없다
visited = [False] * N
# 경로
route = [0] * N
# 비용 배열
min_pay = 1000000000

def calcul_pay(route):
    sum_pay = 0
    start = route[0]
    dep = route[0]
    if payment_arr[route[len(route)-1]][start]:
        for des in range(1, len(route)):
            sum_pay += payment_arr[dep][route[des]]
            dep = route[des]

        sum_pay += payment_arr[dep][start]
        return sum_pay

    else:
        return 1000000000

def make_route(count, start_point, N):
    global min_pay
    if count == N:
        min_pay = min(min_pay, calcul_pay(route))

        return

    for i in range(1, N):
        if visited[i] or i == start_point or payment_arr[start_point][i] == 0:
            continue

        route[count] = i
        visited[i] = True
        start_point = i
        make_route(count+1, start_point, N)
        visited[i] = False


make_route(1, 0, N)

print(min_pay)
'''