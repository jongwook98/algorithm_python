from sys import stdin

def find_GCP(A, B):
    R = A % B
    if R == 0:
        return B
    else:
        return find_GCP(B, R)

def main():
    Test_case = int(stdin.readline())
    for _ in range(Test_case):
        A, B = map(int, stdin.readline().split())
        if B > A:
            temp = A
            A = B
            B = temp

        GCP = find_GCP(A, B)
        print(round(A*B/GCP))


if __name__ == "__main__":
    main()