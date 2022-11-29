# E<= 15, S <= 28, M <= 19

from sys import stdin

E, S, M = map(int, stdin.readline().split())

# 입력받은 E 는 X % 15 S 는 X % 28 M 은 X % 19
count = 0
while True:
    year = 28 * count + S
    if year % 19 == M or (year % 19 == 0 and M == 19):
        if year % 15 == E or (year % 15 == 0 and E == 15):
            print(28*count + S)
            break

    count += 1