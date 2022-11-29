tall_list = [0] * 9
for i in range(9):
    tall_list[i] = int(input())

tall_list.sort()
# 키 입력 받고 정렬

# 일곱난쟁이의 키 100 인 인원 찾기
false_drawf1 = 7; false_drawf2 = 8

while True:
    is_dwarf = [1] * 9
    is_dwarf[false_drawf1] = 0; is_dwarf[false_drawf2] = 0
    sum_height = 0
    for i in range(9):
        if is_dwarf[i]:
            sum_height += tall_list[i]

    if sum_height == 100:
        break

    else:
        if false_drawf1 > 0:
            false_drawf1 -= 1
        else:
            false_drawf1 = false_drawf2-2
            false_drawf2 = false_drawf2-1

for i in range(9):
    if is_dwarf[i]:
        print(tall_list[i])