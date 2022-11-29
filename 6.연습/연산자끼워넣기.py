from sys import stdin

N = int(stdin.readline())
num_arr = list(map(int, stdin.readline().split()))
items = list(map(int, stdin.readline().split()))

sig_arr = []

max_cal = -1000000000
min_cal = 1000000000

for sig in range(4):
    for _ in range(items[sig]):
        sig_arr.append(sig)

def next_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a) - 1
    while a[j] <= a[i-1]:
        j -= 1
    a[j], a[i-1] = a[i-1], a[j]

    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True

def calcul(num_arr, sig_arr):
    global max_cal
    global min_cal

    cal = num_arr[0]

    for n in range(len(sig_arr)):
        if sig_arr[n] == 0:
            cal = cal + num_arr[n+1]
        elif sig_arr[n] == 1:
            cal = cal - num_arr[n+1]
        elif sig_arr[n] == 2:
            cal = cal * num_arr[n+1]
        else:
            if cal < 0 and num_arr[n+1] >= 0:
                cal = -(abs(cal) // num_arr[n+1])
            else:
                cal = cal // num_arr[n+1]

    max_cal = max(max_cal, cal)
    min_cal = min(min_cal, cal)

    return

calcul(num_arr, sig_arr)
while next_permutation(sig_arr):
    calcul(num_arr, sig_arr)

print(max_cal)
print(min_cal)