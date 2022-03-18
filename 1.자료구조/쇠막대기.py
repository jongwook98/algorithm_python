from sys import stdin

STR = list(stdin.readline().strip())
stack_iron = 0
part_iron = 0

for i in range(len(STR)):
    if STR[i] == '(':
        stack_iron = stack_iron + 1
    elif STR[i] == ')':
        stack_iron = stack_iron - 1
        if STR[i-1] == '(':
            part_iron += stack_iron
        else:
            part_iron += 1
print(part_iron)