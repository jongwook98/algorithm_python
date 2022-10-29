''' 내가 푼것
def solution(n, arr1, arr2):
    Map = [[False for _ in range(n)] for _ in range(n)]

    for y, dec in enumerate(arr1):
        for x, num in enumerate(bin(dec)):
            if x > 1:
                if Map[y][x - (len(bin(dec)) - n)] is False and num == '1':
                    Map[y][x - (len(bin(dec)) - n)] = True

    for y, dec in enumerate(arr2):
        for x, num in enumerate(bin(dec)):
            if x > 1:
                if Map[y][x - (len(bin(dec)) - n)] is False and num == '1':
                    Map[y][x - (len(bin(dec)) - n)] = True

    answer = []
    for y in range(n):
        str = ''
        for x in range(n):
            if Map[y][x] is True:
                str += '#'
            else:
                str += ' '
        answer.append(str)

    return answer
'''

def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer

# zip 합쳐주는 함수
# bin(i|j) 이진수 or
# rjust(숫자, '0') 오른쪽 정렬 공백은 '0'으로 채워넣음
