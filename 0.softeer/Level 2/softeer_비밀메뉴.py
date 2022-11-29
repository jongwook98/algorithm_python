from sys import stdin

M, N, K = map(int, stdin.readline().split())
secret_arr = list(map(int, stdin.readline().split()))
input_button = list(map(int, stdin.readline().split()))

out_menu = False

for i in range(len(input_button) - M + 1):
    for n in range(M):
        if input_button[i + n] != secret_arr[n]:
            out_menu = False
            break
        else:
            out_menu = True

    if out_menu:
        break

if out_menu:
    print("secret")
else:
    print("normal")
