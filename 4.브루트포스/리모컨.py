from sys import stdin

channel = int(stdin.readline())
broken_button_num = int(stdin.readline())
is_pushable = [num for num in range(10)]

if broken_button_num:
    broken_button_arr = list(map(int, stdin.readline().split()))

    for i in broken_button_arr:
        is_pushable.remove(i)

# 버튼으로 이동할 수 있는 차이가 가장 적은 채널 구하고 min 1
# 현재 채널에서 이동하는 경우의 수보다 적은지 비교  min 2 abs(channel - 100)

def push_count(num):
    count = 0
    if num == 0:
        return 1
    while num:
        count += 1
        num = num // 10
        if num == 0:
            return count

min_push = abs(channel - 100)

try:
    if is_pushable[0]:
        not_last_push = [0] + is_pushable
    else:
        not_last_push = is_pushable
except:
    not_last_push = [0]

# 현재 문제 0 버튼이 빠졌을 때 누르지 않는 것을 고려해야함

def is_possilbe(num):
    while num:
        try:
            is_pushable.index(num % 10)
        except:
            return False
        num = num // 10
    return True

for a in not_last_push:
    for b in not_last_push:
        for c in not_last_push:
            for d in not_last_push:
                for e in not_last_push:
                    for f in is_pushable:
                        make_channel = a * 100000 + b * 10000 + c * 1000 + d * 100 + e * 10 + f
                        if is_possilbe(make_channel):
                            push_button = push_count(make_channel)
                            min_push = min(min_push, push_button + abs(make_channel - channel))

print(min_push)