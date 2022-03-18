Test_case = int(input())
string = []

for t in range(Test_case):
    sentence = input().split()
    for w in sentence:
        for p in range(1, len(w)+1):
            print(w[-p], end='')
        print(end=' ')
    print()