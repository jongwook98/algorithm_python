'''
def solution(id_list, report, k):
    my_dict = {}
    user_dict = {}
    user_score = {}
    score = {}
    answer = [0 for _ in range(len(id_list))]

    for info in id_list:
        user_dict[info] = []
        user_score[info] = 0
        score[info] = 0

    for info in report:
        if info.split()[1] in user_dict[info.split()[0]]:
            continue

        user_dict[info.split()[0]].append(info.split()[1])
        user_score[info.split()[1]] += 1

    for key, value in user_score.items():
        if value >= k:
            for pre, pre_list in user_dict.items():
                for is_exist in pre_list:
                    if key == is_exist:
                        score[pre] += 1

    for num, value in enumerate(score.values()):
        answer[num] = value
    return answer
'''

# 내 코드와 다른점
# set을 이용해 중복처리, 반복문을 이용하여

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer

#solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)
solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)