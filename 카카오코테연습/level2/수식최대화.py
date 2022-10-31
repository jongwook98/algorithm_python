from itertools import permutations
from collections import Counter
import re

def cal(numarr, express, priority):
    maximum = 0

    for per in priority:
        #print(per)
        arr = numarr[:]
        exp = express[:]
        for sign in per:
            while sign in exp:
                index = exp.index(sign)

                if sign == '-':
                    arr[index] = arr[index] - arr[index + 1]
                    arr.pop(index + 1)
                    exp.pop(index)
                elif sign == '+':
                    arr[index] = arr[index] + arr[index + 1]
                    arr.pop(index + 1)
                    exp.pop(index)
                elif sign == '*':
                    arr[index] = arr[index] * arr[index + 1]
                    arr.pop(index + 1)
                    exp.pop(index)

        result = arr[0]
        maximum = max(maximum, abs(result))

    return maximum

def solution(expression):

    numarr = list(map(int, re.sub('[^0-9]', ' ', expression).split()))
    express = re.sub('[0-9]', ' ', expression).split()

    return cal(numarr, express, permutations(['+', '-', '*'], 3))
