# 누적합으로 재생 시간 계산
# 구간합 투포인터로 재생 시간 많은 구간 출력

import re


def solution(play_time, adv_time, logs):
    total_time = list(map(int, re.sub('[^0-9]', ' ', play_time).split()))
    total = total_time[0] * 3600 + total_time[1] * 60 + total_time[2]

    adv_t = list(map(int, re.sub('[^0-9]', ' ', adv_time).split()))
    adv = adv_t[0] * 3600 + adv_t[1] * 60 + adv_t[2]

    sub_add = [0 for _ in range(total + 2)]

    for log in logs:
        run_time = list(map(int, re.sub('[^0-9]', ' ', log).split()))

        start = run_time[0] * 3600 + run_time[1] * 60 + run_time[2]
        fin = run_time[3] * 3600 + run_time[4] * 60 + run_time[5]

        sub_add[start + 1] += 1
        sub_add[fin + 1] -= 1

    for i in range(1, len(sub_add)):
        sub_add[i] += sub_add[i - 1]

    part_add = [0 for _ in range(len(sub_add))]

    part_add[0] = sub_add[0]
    for i in range(1, len(sub_add)):
        part_add[i] += part_add[i - 1] + sub_add[i]

    sp, ep = 0, adv
    max_play, answer = 0, 0
    for i in range(total - adv + 1):
        if max_play != max(max_play, part_add[ep] - part_add[sp]):
            max_play = max(max_play, part_add[ep] - part_add[sp])

            answer = sp

        sp += 1
        ep += 1

    hour = str(answer // 3600).rjust(2, "0")
    minute = str(answer % 3600 // 60).rjust(2, "0")
    second = str(answer % 60).rjust(2, "0")

    answer = hour + ":" + minute + ":" + second
    return answer
