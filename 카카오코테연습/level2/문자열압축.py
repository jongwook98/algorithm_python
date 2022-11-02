def find_short(lst, step):
    left, right = 0, step
    string = ''

    last = ''
    fin = len(lst)

    cnt = 1

    while right <= fin:
        cur = lst[left:right]
        if last == cur:
            cnt += 1

        elif cnt > 1:
            string += str(cnt) + last
            cnt = 1

        else:
            string += last

        last = cur

        left += step
        right += step

    if cnt > 1:
        string += str(cnt) + cur + lst[left:]

    else:
        string += cur + lst[left:]

    return len(string)

def solution(s):
    answer = 1001

    if len(s) == 1:
        return 1

    for i in range(1, len(s) // 2 + 1):
        answer = min(answer, find_short(s, i))

    return answer