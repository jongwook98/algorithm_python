# 정확성 40/40 , 효율성 0/60 풀이

# 효율성을 높이려면 -> 이진 탐색으로 바꾸어 계산해야하며
# 지원조건에 상관없는 것에 대해 똑같이 값을 추가해야함 -> 처음 지원자를 해당하는 dict구조에 넣을때
# 자신의 지원조건 dict 과 상관없음 dict에 넣어서 모집 요건이 상관 없음 일 때, 그대로 사용할 수 있도록 해야함

from collections import defaultdict

lang = {"cpp": 0o1000, "java": 0o2000, "python": 0o4000, "-": 0o7000}
job = {"backend": 0o100, "frontend": 0o200, "-": 0o700}
exp = {"junior": 0o10, "senior": 0o20, "-": 0o70}
food = {"chicken": 0o1, "pizza": 0o2, "-": 0o7}

spec = [lang, job, exp, food]


def bit_and(info, query):
    if info & query != info:
        return False

    return True


def solution(info, query):
    appliers = defaultdict(int)
    for careers in info:
        career = careers.split()
        appliers[lang[career[0]] + job[career[1]]
                 + exp[career[2]] + food[career[3]], int(career[4])] += 1

    appliers = sorted(appliers.items(), key=lambda x: -x[0][1])

    answer = []
    for recruits in query:
        cnt = 0
        ind = recruits.replace('and', '').split()
        recruit = [lang[ind[0]] + job[ind[1]] + exp[ind[2]] + food[ind[3]], int(ind[4])]

        for applier, value in appliers:
            if applier[1] < recruit[1]:
                break
            if bit_and(applier[0], recruit[0]):
                cnt += value

        answer.append(cnt)

    return answer

''' 다른 사람의 100점 답안지 '''
def solution(info, query):
    data = dict()
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    data.setdefault((a, b, c, d), list())
    for i in info:
        i = i.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        data[(a, b, c, d)].append(int(i[4]))

    for k in data:
        data[k].sort()

        # print(k, data[k])

    answer = list()
    for q in query:
        q = q.split()

        pool = data[(q[0], q[2], q[4], q[6])]
        find = int(q[7])
        l = 0
        r = len(pool)
        mid = 0
        while l < r:
            mid = (r+l)//2
            if pool[mid] >= find:
                r = mid
            else:
                l = mid+1
            # print(l, r, mid, answer)
        # answer.append((pool, find, mid))
        answer.append(len(pool)-l)

    return answer