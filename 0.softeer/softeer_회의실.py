from sys import stdin

N, M = map(int, stdin.readline().split())  # N : 회의실, M : 예약된 회의

conference_room = []
conference_time = []

reservation = []

for i in range(N):
    conference_room.append(stdin.readline().strip())
    conference_time.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

conference_room.sort()

for _ in range(M):
    reservation = stdin.readline().strip().split()
    for time in range(int(reservation[2]) - int(reservation[1])):
        conference_time[conference_room.index(reservation[0])][int(reservation[1]) - 9 + time] = 1

for n in range(N):
    flag = 0
    sep_time = 0
    useable_time = []
    print("Room ", conference_room[n], ":", sep="")
    for t in range(9):
        if conference_time[n][t] == flag:
            sep_time += 1
            if flag == 1:
                useable_time.append(t + 9)
                flag = 0
            else:
                if t == 0:
                    useable_time.append(t + 9)
                else:
                    useable_time.append(t + 9)
                flag = 1

    if len(useable_time) % 2 == 1:
        useable_time.append(18)
    if sep_time:
        print(round(len(useable_time) / 2), "available:")
    else:
        print("Not available")

    for t in range(round((len(useable_time)) / 2)):
        print("{0:02d}-{1:02d}".format(useable_time[t * 2], useable_time[t * 2 + 1]))

    if n != N - 1:
        print("-----")