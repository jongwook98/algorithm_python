from sys import stdin

def prev_permutation(a):
    i = len(a)-1
    while i > 0 and a[i-1] <= a[i]:
        i -= 1
    if i <= 0:
        return False

    j = len(a)-1
    while a[j] >= a[i-1]:
        j -= 1
    a[i-1], a[j] = a[j], a[i-1]
    j = len(a)-1
    while j > i:
        a[i], a[j] = a[j], a[i]
        j -= 1
        i += 1

    return True


def cal_cul_sta(sta_arr, team):
    sta_sum = 0
    for count, i in enumerate(team[:-1]):
        for j in team[count+1:]:
            sta_sum += sta_arr[i][j]
            sta_sum += sta_arr[j][i]

    return sta_sum

N = int(stdin.readline())
status_arr = [0] * N

A_member = (N//2)

team_sep = [1] * A_member + [0] * (N-A_member)
team_A = [i for i in range(A_member)]
team_B = [i for i in range(A_member, N)]

min_sub = 10000000

for i in range(N):
    status_arr[i] = list(map(int, stdin.readline().split()))

while True:
    min_sub = min(min_sub, abs(cal_cul_sta(status_arr, team_A) - cal_cul_sta(status_arr, team_B)))
    if min_sub == 0:
        break

    if not prev_permutation(team_sep):
        A_member += 1
        if A_member >= (N-1):
            break
        team_sep = [1] * A_member + [0] * (N - A_member)
        team_A = [i for i in range(A_member)]
        team_B = [i for i in range(A_member, N)]

    team_A = []; team_B = []
    for i in range(N):
        if team_sep[i]:
            team_A.append(i)
        else:
            team_B.append(i)

print(min_sub)