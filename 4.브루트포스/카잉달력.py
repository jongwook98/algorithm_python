from sys import stdin

Test_case = int(stdin.readline())

def cal_date(M, N, x, y):
    x_year = x
    y_year = y

    while True:
        if x_year == y_year:
            return x_year

        elif x_year >= M*N:
            return -1

        elif x_year < y_year:
            x_year += M

        else:
            y_year += N

for _ in range(Test_case):
    M, N, x, y = map(int, stdin.readline().split())
    print(cal_date(M, N, x, y))