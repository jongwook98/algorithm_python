from sys import stdin

N, M = map(int, stdin.readline().split())  # N : 회의실, M : 예약된 회의

conference_room = []
conference_time = []

useable_time = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

reservation = []

for i in range(N):
    conference_room.append(stdin.readline().strip())
    conference_time.append(useable_time)

for _ in range(M):
    reservation = stdin.readline().strip().split()
    for time in range(int(reservation[2]) - int(reservation[1]) + 1):
        # print(int(reservation[1])-9+time)
        conference_time[conference_room.index(reservation[0])][int(reservation[1]) - 9 + time] = 1

    # print(reservation)

print(conference_room)
print(conference_time)