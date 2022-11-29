'''
16 -> 8 -> 4 -> 2 -> 1

19 -> 18 -> 6 -> 2 -> 1
16 -> 15 -> 5 -> 4 -> 2 -> 1

12 -> 4 -> 2 -> 1
12 -> 6 -> 3 -> 1
'''
# 생각의 흐름
# 3으로 나눌 수 있는 수는 3으로 나누는게 가장 빠를 듯,
# 2로   나눌 수 있는 수는 1을 빼고 3으로 나누는게 빠른 경우가 있음,  10 -> 9 -> 3 -> 1 ..... 10 -> 5 -> 4 -> 2 -> 1
#                                                           28 -> 27 -> 9 -> 3 -> 1 .. 28 -> 14 -> 7 -> 6 -> 2 -> 1
#                                                           46 -> 45 -> 15 -> 5 -> 4 -> 2 -> 1 46 -> 23 -> 22 -> 11 -> 10 -> 9 -> 3 -> 1

# 다이나믹 프로그래밍의 bottom up 으로 구현하여 작은 수부터 미리 구해놔서 최단 루트의 개수를 세고 3가지 경우의 대한 값의 수가 가장 작은 길로 가자!

short_route = [0 for _ in range(1000001)]

def find_short_route(num):
    possible_route = []
    if not num % 3:
        possible_route.append(short_route[num//3])
    if not num % 2:
        possible_route.append(short_route[num//2])
    possible_route.append(short_route[num-1])

    return min(possible_route) + 1

N = int(input())

if N == 1:
    print(0)
else:

    for i in range(2, N):
        if not short_route[i]:
            short_route[i] = find_short_route(i)

    print(find_short_route(N))