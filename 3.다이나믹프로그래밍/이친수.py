# 1로 시작해야하기 때문에 N == 1 일 때 0으로 끝나는 수 는 0, 1로 끝나는 수는 1
# 0으로 끝나는 수는 1, 0 둘다 가능 1로 끝나는 수는 0만 가능

# binary_arr[i][0] = binary_arr[i-1][0] + binary_arr[i-1][1]
# binary_arr[i][1] = binary_arr[i-1][0]

binary_arr = [[0]*2 for _ in range(91)]

binary_arr[1][0] = 0; binary_arr[1][1] = 1
for i in range(2, 91):
    binary_arr[i][0] = binary_arr[i-1][0] + binary_arr[i-1][1]
    binary_arr[i][1] = binary_arr[i-1][0]

N = int(input())
print(sum(binary_arr[N]))