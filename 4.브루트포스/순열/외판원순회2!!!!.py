
# 입력 N의 범위가 10 이하이므로 팩토리얼 까지 가능 -> 10 이므로 10 X 10! 는 약 3.5 초가 넘어감
# 시간초과

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
min_pay = 100000000

def calcul_pay(route):
    sum_pay = 0
    start = route[0]
    dep = route[0]
    for des in range(1, len(route)):
        sum_pay += payment_arr[dep][route[des]]
        dep = route[des]

    sum_pay += payment_arr[dep][start]
    return sum_pay

def make_route(count, start_point, N):
    global min_pay
    if count == N:
        min_pay = min(min_pay, calcul_pay(route))

        return

    for i in range(0, N):
        if visited[i] or i == start_point or payment_arr[start_point][i] == 0:
            continue

        route[count] = i
        visited[i] = True
        start_point = i
        make_route(count+1, start_point,N)
        visited[i] = False

for i in range(N):
    make_route(0, i, N)

print(min_pay)
