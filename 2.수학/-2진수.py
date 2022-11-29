<<<<<<< HEAD
N=int(input())
ans=''
if N==0:
    print(0)
    exit()

while N!=0:
    if N%-2:
        N=N//-2+1
        ans='1'+ans
    else:
        N//=-2
        ans='0'+ans

print(int(ans))

''' 아래는 내가 구현한 코드인데,, 틀렸다고 한다. 이유를 생각해보자
num = int(input())
num_array = []

while num:
    num_array.append(num % 2)
    if num % -2:
        num = num // -2 + 1
    else:
        num = num // -2

for i in range(len(num_array) - 1, -1, -1):
    print(int(num_array[i]), end='')
=======
N=int(input())
ans=''
if N==0:
    print(0)
    exit()

while N!=0:
    if N%-2:
        N=N//-2+1
        ans='1'+ans
    else:
        N//=-2
        ans='0'+ans

print(int(ans))

''' 아래는 내가 구현한 코드인데,, 틀렸다고 한다. 이유를 생각해보자
num = int(input())
num_array = []

while num:
    num_array.append(num % 2)
    if num % -2:
        num = num // -2 + 1
    else:
        num = num // -2

for i in range(len(num_array) - 1, -1, -1):
    print(int(num_array[i]), end='')
>>>>>>> feb7b03d3ac8b082d54e5e67b97fd44c0252cf76
'''