from sys import stdin
import math

def prime(A):
    if A == 2:
        return True
    if A < 2:
        return False

    for n in range(2, round(math.sqrt(A))+1):
        if A % n == 0:
            return False

    return True

def main():
    number = 0
    Test_case = int(stdin.readline())
    prime_num = list(map(int, stdin.readline().split()))

    for i in range(Test_case):
        if prime(prime_num[i]):
            number += 1

    print(number)

if __name__ == "__main__":
    main()