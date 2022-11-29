n = int(input(),2) # int( ,2) 로 이진수로 바꿔주고
print(oct(n)[2:])  # oct 를 앞에 표기를 날리는 포맷팅

'''
num_of_binary = input().strip() # 직접 포맷팅 구현.....

octal = []
count = 0
output = []

def binary_to_octal(list):
    num = 1
    result = 0
    for i in range(len(list)):
        result = result + (int(list[i]) * num)
        num = num * 2

    return result

for i in range(len(num_of_binary)-1, -1, -1):
    octal.append(num_of_binary[i])
    count += 1
    if count == 3:
        output.append(binary_to_octal(octal))
        octal = []
        count = 0

if octal:
    output.append(binary_to_octal(octal))

for i in range(len(output)-1, -1, -1):
    print(output[i], end= "")
'''
