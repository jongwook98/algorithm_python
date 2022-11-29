from sys import stdin

N, M = map(int, stdin.readline().split())

limit_v = [];
limit_d = []
act_v = [];
act_d = []

max_vel_sub = 0
l_index = 0;
a_index = 0

for i in range(N):
    D, V = map(int, stdin.readline().split())
    limit_d.append(D);
    limit_v.append(V)

for i in range(M):
    D, V = map(int, stdin.readline().split())
    act_d.append(D);
    act_v.append(V)

while True:

    move_distance = min(limit_d[l_index], act_d[a_index])
    limit_d[l_index] -= move_distance;
    act_d[a_index] -= move_distance

    if max_vel_sub < act_v[a_index] - limit_v[l_index]:
        max_vel_sub = act_v[a_index] - limit_v[l_index]

    if limit_d[l_index] == 0:
        l_index += 1
    if act_d[a_index] == 0:
        a_index += 1

    if l_index >= len(limit_d):
        break

print(max_vel_sub)