from sys import stdin

num_of_zero = 0
factorial_num = int(stdin.readline())

for i in range(1, factorial_num+1):
    while True:
        if i % 5 == 0:
            num_of_zero += 1
            i /= 5
        else:
            break

print(num_of_zero)