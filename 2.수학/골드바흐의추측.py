from sys import stdin

# 범위 안에서 소수 찾기
#


while True:
    even_num = int(stdin.readline())

    if even_num == 0:
        break

    if (even_num % 2 == 0):
            print("Goldbach's conjecture is wrong.")