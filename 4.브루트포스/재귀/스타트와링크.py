# 스타트팀과 링크팀을 각각 1, 0 팀으로 두고 모든 순열을 구한다? 1 과 0으로

from sys import stdin
def prev_premutation(arr):
    i = len(arr)-1
    while i > 0 and arr[i-1] <= arr[i]:
        i -= 1
    if i <= 0:
        return False

    j = len(arr)-1
    while arr[j] >= arr[i-1]:
        j -= 1
    arr[i-1], arr[j] = arr[j], arr[i-1]
    j = len(arr) -1
    while i < j:
        arr[j], arr[i] = arr[i], arr[j]
        j -= 1
        i += 1

    return True

def cal_cul_sum(sta_arr, team):
    sum_status = 0
    for count, i in enumerate(team[:-1]):
        for j in team[count+1:]:
            sum_status += sta_arr[i][j]
            sum_status += sta_arr[j][i]

    return sum_status

N = int(stdin.readline())

status_arr = [0] * N
team_sep = [1] * (N//2) + [0] * (N//2)

team_A = [i for i in range(N//2)]
team_B = [i for i in range((N//2), N)]

for i in range(N):
    status_arr[i] = list(map(int, stdin.readline().split()))

min_sub = 10000000

while True:
    min_sub = min(min_sub ,abs(cal_cul_sum(status_arr, team_A) - cal_cul_sum(status_arr, team_B)))
    if not prev_premutation(team_sep):
        break
    team_A = []; team_B = []
    for i in range(len(team_sep)):
        if team_sep[i]:
            team_A.append(i)
        else:
            team_B.append(i)

print(min_sub)