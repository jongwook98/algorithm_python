def solution(n, t, m, p):

    def find_str(to_, from_):
        str_ = ''
        while from_ > 0:
            if from_ % to_ > 9:
                str_ += chr(ord('A') + from_ % to_ - 10)
            else:
                str_ += str(from_ % to_)
            from_ //= to_

        return str_[::-1]

    max_len = t * m

    find_num = '0'
    num = 0
    while len(find_num) < max_len:
        find_num += find_str(n, num)
        num += 1

    answer = ''
    for i in range(t):
        answer += find_num[m * i + p - 1]

    return answer
