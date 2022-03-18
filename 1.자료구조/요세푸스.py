from sys import stdin

command = list(map(int, stdin.readline().split()))
total_list = list(range(1, int(command[0])+1))
out_list = []
out_string = '<'
pop_num = 0

for _ in range(int(command[0])):
    pop_num = pop_num + int(command[1]-1)

    if pop_num >= len(total_list):
        pop_num = pop_num%len(total_list)

    out_list.append(total_list.pop(pop_num))
    if pop_num >= len(total_list):
        pop_num = 0

for i in range(len(out_list)):
    out_string = out_string + str(out_list[i]) + ', '

print(out_string[:-2],end = '>')