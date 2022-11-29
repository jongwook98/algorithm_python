from sys import stdin

max_pay = 0
def work(now, endday, pay, T, P):
    global max_pay
    if now > endday:
        return
    elif now == endday:
        max_pay = max(max_pay, pay)
        return

    max_pay = max(max_pay, pay)

    work(now+T[now], endday, pay+P[now], T, P) # 일 함
    work(now+1, endday, pay, T, P) # 일 안함

N = int(stdin.readline())
T = [0] * N; P = [0] * N
for i in range(N):
    T[i], P[i] = map(int, stdin.readline().split())

work(0, N, 0, T, P)
print(max_pay)

'''
백준 재귀 강의를 보기전 풀이 구현하지 못함
from sys import stdin

N = int(stdin.readline()) # 상담 일자
T = [0] * N; P = [0] * N  # 기간, 돈

sum_pay = [[0] * (N+1)] * (N+1) # 1~N 일 부터 일 시작하는 순간의 max 값 구하기
max_pay = 0

for i in range(N):
    T[i], P[i] = map(int, stdin.readline().split())

def max_pay_detect(stand_day, day, N):
    global max_pay
    if day >= N:
        sum_pay[stand_day][0] = max(sum_pay[stand_day])
        return

    for i in range(day, N+1):
        #if day + T[i] > N:
        #    sum_pay[start_day]
        #    continue
        sum_pay[stand_day][i] = sum_pay[stand_day] + P[i]
        max_pay_detect(stand_day, day+T[i], N)

max_pay_detect(0, 0, N)
print(max_pay)
'''