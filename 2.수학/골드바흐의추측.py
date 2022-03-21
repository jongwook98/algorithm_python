from sys import stdin
#구현은 성공했지만 시간초과가 발생한 코드 시간초과 문제를 해결하려면 에라토스테네스의 체를 적용시켜야 함

# 범위 안에서 소수 찾기
array = [True for i in range(1000001)] #에라토스테네스의 체

for i in range(2, 1001):
    if array[i]:
        for k in range(i + i, 1000001, i):
            array[k] = False

while True:
    even_num = int(stdin.readline())

    if even_num == 0: break

    for i in range(3, len(array)):
        if array[i] and array[even_num-i]:
            print(even_num, "=", i, "+", even_num-i)
            break