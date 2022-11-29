#                                   모두 세로 하나만 가로 두개가 가로 새개가 가로 .. 네개가 가로
# 2 x 2 일 때 채울 수 있는 방법 2가지      1   2C0     1  1C1  0          0
# 2 x 3 일 때 채울 수 있는 방법 2가지      1   3C0     2  2C1  0          0
# 2 x 4일 때 채울 수 있는 방법 5가지      1   4C0     3  3C1  1  2C2     0
# 2 x 5 일 때 채울 수 있는 방법           1   5C0     4  4C1  3  3C2     0
# 2 x 6 일 때 채울 수 있는 방법           1   6C0     5  5C1  6  4C2     1 3C3
# 2 x 7 일 때 채울 수 있는 방법           1   7C0     6  6C1 10  5C2
#                                                                                1
# 2 x 9 일 때 채울 수 있는 방법           1   9C0     8  8C1  21 7C2  20   6C3  5  5C4

'''
n = int(input())
d = [0]*1001
d[0] = 1
d[1] = 1
for i in range(2, n+1):
    d[i] = d[i-1] + d[i-2]
    d[i] %= 10007
print(d[n])
# 백준코드 다이나믹 프로그래밍으로 계산하는게 훨씬 빠른 알고리즘이다.
'''

#내가 구현한 코드지만,,pow의 계산 결과가 분수꼴로 계산되면서 76 부터 부동소수점 계산에 대한 오류가 발생함.-> 그 전에 나머지로 나누어 값이 깔끔해짐,,
#실행 시간으로 비교했을 때 4배 느림,,
def calculation_combination(N, M):
    cal_com = []
    result = 1
    for i in range(2, N+1):
        count = 1
        if i <= M:
            count -= 1
        if i <= N-M:
            count -= 1

        cal_com.append(count)

    for i in range(len(cal_com)):
        if cal_com[i]:
            result = result * (pow(i+2,cal_com[i], 10007))

    return round(result)

def method_fill_rectangle(N):
    result = 0
    for i in range(N//2 + 1):
        result = result + calculation_combination(N-i, i)

    return result

def main():
    N = int(input())
    if N == 1:
        print(1)
    else:
        print(method_fill_rectangle(N)%10007)

if __name__=="__main__":
    main()