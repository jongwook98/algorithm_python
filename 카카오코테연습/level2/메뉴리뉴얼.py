from collections import defaultdict

def solution(orders, course):
    answer = []

    def find_com(order, course, dict_num, menu_list, index):
        if len(menu_list) == course:
            sort_list = sorted(menu_list)
            menu_dict[dict_num][''.join(sort_list)] += 1
            return True
        if index >= len(order):
            return False

        menu_list.append(order[index])
        find_com(order, course, dict_num, menu_list, index + 1)

        menu_list.pop()
        find_com(order, course, dict_num, menu_list, index + 1)


    menu_dict = [defaultdict(int) for _ in range(len(course))]
    new_course = [[] for _ in range(len(course))]

    for order in orders:
        for dict_num, menu_sum in enumerate(course):
            find_com(order, menu_sum, dict_num, list(), 0)

    for i in range(len(course)):
        new_course[i] = sorted(menu_dict[i].items(), key = lambda x: (-x[1], x[0]))
        if new_course[i]:
            maximum = new_course[i][0][1]

            if maximum >= 2:
                for j in range(len(new_course[i])):
                    if maximum == new_course[i][j][1]:
                        answer.append(new_course[i][j][0])

    answer.sort()

    return answer

# 다른 사람의 풀이 -> collectios 의 counter, most_common(), itertools 의 combinations을 이용하여 문제 풀이
import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]

