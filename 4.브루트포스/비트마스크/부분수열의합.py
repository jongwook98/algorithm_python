from sys import stdin

count = 0

def cal_cul(num_arr, index, sum_, use,target):
    global count
    if index == len(num_arr):
        if use:
            if sum_ == target:
                count += 1
        return True

    cal_cul(num_arr, index+1, sum_+num_arr[index], use+1,target)
    cal_cul(num_arr, index+1, sum_, use, target)

N, S = map(int, stdin.readline().split())
num_arr = list(map(int, stdin.readline().split()))

cal_cul(num_arr, 0, 0, 0,S)
print(count)