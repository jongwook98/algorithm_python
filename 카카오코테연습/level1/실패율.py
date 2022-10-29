def solution(N, stages):
    answer = [i for i in range(1, N + 1)]
    passer = 0
    diff = {}

    for i in range(N + 1, 0, -1):
        challenger = stages.count(i)
        passer += stages.count(i)

        if i == N + 1:
            continue

        if passer != 0:
            diff[i] = challenger / passer
        else:
            diff[i] = 0

    answer = sorted(answer, key =lambda x: (-diff[x], x))

    return answer

# sorted lambda 잘 사용하기, 앞에 - 을 붙이면 reverse되어 정렬한다..