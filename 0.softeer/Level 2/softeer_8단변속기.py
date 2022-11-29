from sys import stdin

vel_ = list(map(int, stdin.readline().split()))

start_num = vel_[0]
status = 0

for i in range(1, len(vel_)):
    if abs(vel_[i] - start_num) == 1:
        start_num = vel_[i]
    else:
        status = 2
        break

if status == 2:
    print("mixed")

else:
    if start_num == 8:
        print("ascending")
    else:
        print("descending")