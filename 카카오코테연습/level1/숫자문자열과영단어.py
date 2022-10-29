'''
alpha_num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
def alpha_to_num(data, index, return_list):
    if index >= len(data):
        return return_list
    for i in range(10):
        flag = True
        for j in range(len(alpha_num[i])):
            if data[index + j] != alpha_num[i][j]:
                flag = False
                break
        if flag is True:
            return_list.append(i)
            alpha_to_num(data, index + len(alpha_num[i]), return_list)
            break
def solution(s):
    alpha = []
    answer = []
    return_list = []
    for char in s:
        if char.isalpha():
            alpha.append(char)
        else:
            if len(alpha):
                alpha_to_num(alpha, 0, return_list)
                alpha.clear()
                answer = answer + return_list
                return_list.clear()
            answer.append(int(char))
    if len(alpha):
        (alpha_to_num(alpha, 0, return_list))
        alpha.clear()
        answer = answer + return_list
        return_list.clear()
    return int(''.join(map(str, answer)))
'''

#간단하게 딕셔너리로 구현 가능..!

num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    print(int(answer))

solution(input())