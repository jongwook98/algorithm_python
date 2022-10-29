base = ["RT", "CF", "JM", "AN"]
MBTI = {"RT":0, "TR":0, "CF":1, "FC":1, "JM":2, "MJ":2, "AN":3, "NA":3}
index = [None, -3, -2, -1, 0, 1, 2, 3]

score = [0, 0, 0, 0]
def solution(survey, choices):
    for num, sur in enumerate(survey):
        if sur in base:
            score[MBTI[sur]] += index[choices[num]]
        else:
            score[MBTI[sur]] -= index[choices[num]]

    answer = ""
    for i in range(len(score)):
        if score[i] < 1:
            answer += str(base[i][0])
        else:
            answer += str(base[i][1])

    return answer