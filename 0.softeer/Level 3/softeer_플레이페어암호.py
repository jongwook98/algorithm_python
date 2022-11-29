from sys import stdin

message_ = list(stdin.readline().strip())
input_key_ = list(stdin.readline().strip())
key_ = []
key_map_ = [[0] * 5 for _ in range(5)]
message_arr_ = []

check = [i for i in range(9)] + [i for i in range(10, 26)]

while len(input_key_):
    cur = ord(input_key_.pop(0)) - 65
    if cur in check:
        check.remove(cur)
        key_.append(chr(cur + 65))

while len(check):
    cur = check.pop(0)
    key_.append(chr(cur + 65))

for y in range(5):
    for x in range(5):
        index_ = y * 5 + x
        key_map_[y][x] = key_[index_]

while len(message_):
    cur_m_1 = message_.pop(0)
    if len(message_):
        if cur_m_1 == message_[0]:
            if cur_m_1 == 'X':
                message_arr_.append((cur_m_1, 'Q'))
            else:
                message_arr_.append((cur_m_1, 'X'))
        else:
            cur_m_2 = message_.pop(0)
            message_arr_.append((cur_m_1, cur_m_2))
    else:
        message_arr_.append((cur_m_1, 'X'))

message_ = []

while len(message_arr_):
    flag = 1
    cur_m_1, cur_m_2 = message_arr_.pop(0)

    m_1_y, m_1_x = False, False
    m_2_y, m_2_x = False, False

    for i in range(5):
        x_arr = [key_map_[i][j] for j in range(5)]

        if cur_m_1 in x_arr and cur_m_2 in x_arr:
            in_1 = x_arr.index(cur_m_1)
            in_2 = x_arr.index(cur_m_2)

            message_.append(key_map_[i][(in_1 + 1) % 5])
            message_.append(key_map_[i][(in_2 + 1) % 5])

            flag = 0
            break

    if flag:

        for i in range(5):
            y_arr = [key_map_[j][i] for j in range(5)]

            if cur_m_1 in y_arr and cur_m_2 in y_arr:
                in_1 = y_arr.index(cur_m_1)
                in_2 = y_arr.index(cur_m_2)

                message_.append(key_map_[(in_1 + 1) % 5][i])
                message_.append(key_map_[(in_2 + 1) % 5][i])

                flag = 0
                break

    if flag:
        for i in range(5):
            x_arr = [key_map_[i][j] for j in range(5)]

            if cur_m_1 in x_arr:
                m_1_y, m_1_x = i, x_arr.index(cur_m_1)
            if cur_m_2 in x_arr:
                m_2_y, m_2_x = i, x_arr.index(cur_m_2)

    if flag:
        message_.append(key_map_[m_1_y][m_2_x])
        message_.append(key_map_[m_2_y][m_1_x])

print(''.join(message_))
