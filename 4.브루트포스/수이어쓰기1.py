def cal_num_size(num):
    count = 1
    sum_size = 0
    while num:
        if num >= (10**count) - (10**(count-1)):
            sum_size += count * ((10**count) - (10**(count-1)))
            num -= (10**count) - (10**(count-1))
            count += 1
        else:
            sum_size += (num*count)
            break

    return sum_size

def main():
    N = int(input())
    print(cal_num_size(N))

if __name__=="__main__":
    main()