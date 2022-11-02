# 정확성 50/100 답안지
#

from collections import defaultdict
from itertools import combinations


def solution(relation):
    answer = 0

    result = [0 for _ in range(len(relation[0]))]
    index = [i for i in range(len(relation[0]))]

    user_dict = defaultdict(set)

    for num in range(1, len(index) + 1):
        for comb in combinations(index, num):
            for rela in relation:
                string = ''
                for idx in range(len(rela)):
                    if idx in comb:
                        string += rela[idx] + ' '

                user_dict[comb].add(string)

            if len(user_dict[comb]) == len(relation):
                for idx in comb:
                    min_list = []
                    flag = True
                    if result[idx] == 1:
                        flag = False
                        break
                    else:
                        min_list.append(idx)
                if flag is True:
                    for idx in min_list:
                        result[idx] = 1
                    answer += 1

    return answer

# 다른사람 코드들,,
###############################1
def solution(relation):
    def is_powerset(parent, child):
        return parent | child == parent


    n_attr = len(relation[0])
    candidate_key = []

    for key in range(1, 1 << n_attr):
        # 현재까지 찾은 후보키을 부분집합으로 가지지 않는지를 먼저 판단
        flag = False
        for e in candidate_key:
            if is_powerset(key, e):
                flag = True
                break
        if flag:
            continue

        # 현재 키가 유일성을 만족하는지를 판단
        sliced_relation = []
        for row in relation:
            sliced_row = []
            for j in range(0, n_attr):
                # print(bin(copied_key >> j))
                if (key >> j) & 1 == 1:
                    sliced_row.append(row[j])
            sliced_relation.append(tuple(sliced_row))

        if len(sliced_relation) != len(set(sliced_relation)):
            continue

        # 후보키 목록에 추가
        candidate_key.append(key)

    answer = len(candidate_key)
    return answer

###################################2
from collections import deque
from itertools import combinations
def solution(relation):
    n_row=len(relation)
    n_col=len(relation[0])  #->runtime error 우려되는 부분

    candidates=[]
    for i in range(1,n_col+1):
        candidates.extend(combinations(range(n_col),i))

    final=[]
    for keys in candidates:
        tmp=[tuple([item[key] for key in keys]) for item in relation]
        if len(set(tmp))==n_row:
            final.append(keys)

    answer=set(final[:])
    for i in range(len(final)):
        for j in range(i+1,len(final)):
            if len(final[i])==len(set(final[i]).intersection(set(final[j]))):
                answer.discard(final[j])

    return len(answer)