from sys import stdin

Test_case = int(input())

zero = [1, 1, 1, 0, 1, 1, 1]
one = [0, 0, 1, 0, 0, 1, 0]
two = [0, 1, 1, 1, 1, 0, 1]
three = [0, 1, 1, 1, 0, 1, 1]
four = [1, 0, 1, 1, 0, 1, 0]
five = [1, 1, 0, 1, 0, 1, 1]
six = [1, 1, 0, 1, 1, 1, 1]
seven = [1, 1, 1, 0, 0, 1, 0]
eight = [1, 1, 1, 1, 1, 1, 1]
nine = [1, 1, 1, 1, 0, 1, 1]
none = [0, 0, 0, 0, 0, 0, 0]

number = [zero, one, two, three, four, five, six, seven, eight, nine, none]

for _ in range(Test_case):
    sw = 0
    A_array = [];
    B_array = []
    A_size = 0;
    B_size = 0

    A, B = map(int, stdin.readline().split())
    A_du = A;
    B_du = B
    while int(A_du):
        A_array.append(round(A_du % 10))
        A_du = int(A_du / 10)
        A_size += 1
    while int(B_du):
        B_array.append(round(B_du % 10))
        B_du = int(B_du / 10)
        B_size += 1

    for _ in range(max(A_size, B_size) - min(A_size, B_size)):
        if A_size < B_size:
            A_array.append(10)  # 10은 none
        else:
            B_array.append(10)

    for i in range(max(A_size, B_size)):
        for l in range(7):
            if number[A_array[i]][l] != number[B_array[i]][l]:
                sw += 1

    print(sw)