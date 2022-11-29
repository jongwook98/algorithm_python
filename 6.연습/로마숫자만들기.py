from sys import stdin

N = int(stdin.readline())

is_consist = []
last_consist = []
next_consist = [0]

num_arr = [1, 5, 10, 50]

for time in range(N):
    last_consist = next_consist
    next_consist = []
    check = [False for _ in range((N * 50) + 1)]

    while len(last_consist):
        j = last_consist.pop()
        for i in range(4):
            if check[j + num_arr[i]] is False:
                check[j + num_arr[i]] = True
                next_consist.append(j + num_arr[i])

                if time == (N-1):
                    is_consist.append(j + num_arr[i])

print(len(is_consist))