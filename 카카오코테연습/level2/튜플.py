from collections import defaultdict
import re

def solution(s):
    answer = []

    dict = defaultdict(int)

    s = re.sub('[^0-9]', ' ', s)
    s = s.split()

    for index in s:
        dict[index] += 1

    dict = sorted(dict.items(), key = lambda x: -x[1])
    for i in dict:
        answer.append(int(i[0]))

    return answer
