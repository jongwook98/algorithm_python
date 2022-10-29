import re


def solution(new_id):
    new_id = new_id.lower()

    new_id = re.sub('[^a-z0-9_.-]', '', new_id)

    while new_id != new_id.replace('..', '.'):
        new_id = new_id.replace('..', '.')

    new_id = new_id.strip('.')

    if not len(new_id):
        new_id = 'a'

    if len(new_id) > 15:
        new_id = new_id[:15]
        new_id = new_id.strip('.')

    if len(new_id) < 3:
        new_id = new_id.ljust(3, new_id[-1])

    print(new_id)
    answer = new_id
    return answer

# 정규식 패턴을 숙지시키면 편할것 같다.