Map = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2),
       7: (2, 0), 8: (2, 1), 9: (2, 2), '*': (3, 0), 0: (3, 1), '#': (3, 2)}

print(Map)

left_num = [1, 4, 7]
right_num = [3, 6, 9]


def solution(numbers, hand):
    left_pos = [3, 0]
    right_pos = [3, 2]

    answer = ''

    for press_num in numbers:
        if press_num in left_num:
            left_pos = Map[press_num]
            answer += 'L'
        elif press_num in right_num:
            right_pos = Map[press_num]
            answer += 'R'

        else:
            y, x = Map[press_num]
            left_dis, right_dis = abs(y - left_pos[0]) + abs(x - left_pos[1]), abs(y - right_pos[0]) + abs(
                x - right_pos[1])
            if left_dis == right_dis:
                if hand == 'left':
                    left_pos = Map[press_num]
                    answer += 'L'
                else:
                    right_pos = Map[press_num]
                    answer += 'R'

            else:
                if left_dis < right_dis:
                    left_pos = Map[press_num]
                    answer += 'L'
                else:
                    right_pos = Map[press_num]
                    answer += 'R'

    return answer