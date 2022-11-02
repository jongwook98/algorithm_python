from collections import deque

def solution(record):
    user = {}
    result = deque()
    answer = []

    for logs in record:
        log = logs.split()
        order = log[0]

        if order == 'Enter':
            user_id = log[1]
            nickname = log[2]
            user[user_id] = nickname
            result.append((0, user_id))
        elif order == 'Leave':
            user_id = log[1]
            result.append((1, user_id))

        elif order == 'Change':
            user_id = log[1]
            nickname = log[2]
            user[user_id] = nickname

    while result:
        order, user_id = result.popleft()
        if order == 0:
            answer.append(user[user_id] + "님이 들어왔습니다.")
        elif order == 1:
            answer.append(user[user_id] + "님이 나갔습니다.")

    return answer