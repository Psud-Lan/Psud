import math
data = {}
file = open('code.txt', 'r')
code = file.read()
file.close()
code = code.split('\n')
for line in range(len(code)):
    code[line] = code[line].split(' ')
printing = 0
print_list = []
looping = False
loop_info = []
def INIT(variable):
    if variable[2][0] == 'i':
        data[variable[1]] = int(variable[2][1:])
    elif variable[2][0] == 's':
        data[variable[1]] = str(variable[2][1:])
    else:
        data[variable[1]] = variable[2]
def IF(condition):
    global num
    skip = int(condition[4])
    if condition[1][0] == 'i':
        val_1 = int(condition[1][1:])
    else:
        val_1 = data[condition[1]]
    if condition[3][0] == 'i':
        val_2 = int(condition[3][1:])
    else:
        val_2 = data[condition[3]]
    op = condition[2]
    if op == '=':
        if val_1 == val_2:
            return
        else:
            num += skip
    elif op == '<':
        if val_1 < val_2:
            return
        else:
            num += skip
    elif op == '>':
        if val_1 > val_2:
            return
        else:
            num += skip
    elif op == '><':
        if val_1 != val_2:
            return
        else:
            num += skip
    elif op == '<=':
        if val_1 <= val_2:
            return
        else:
            num += skip
    elif op == '>=':
        if val_1 >= val_2:
            return
        else:
            num += skip
def PRINT(print_list, sep):
    if sep == '0':
        sep = ''
    else:
        sep = chr(int(sep))
    end_list = []
    for char in range(len(print_list)):
        if print_list[char][1] == 'ASC':
            end_list.append(chr(data[print_list[char][0]]))
        elif print_list[char][1] == 'RAW':
            end_list.append(str(data[print_list[char][0]]))
    print(sep.join(end_list))
def __init__LOOP(rec, amn, loops):
    global loop_info, current_info, looping
    loop_info = [rec, amn, loops - 1]
    current_info = [rec, amn, loops - 1]
    looping = True
def LOOP():
    global current_info, looping, num
    if num == current_info[0] + current_info[1]:
        num = current_info[0]
        current_info[2] -= 1
        if current_info[2] == 0:
            looping = False
        else:
            current_info = [loop_info[0], loop_info[1], current_info[2]]
def VAR(line):
    global val
    coord = line[1]
    op = line[2]
    if line[3][0] == 'i':
        val = int(line[3][1:])
    elif line[3][0] == 's':
        val = int(line[3][1:])
    else:
        val = data[line[3]]
    if op == '+':
        data[coord] += val
    elif op == '-':
        data[coord] -= val
    elif op == '*':
        data[coord] *= val
    elif op == '=':
        data[coord] = val
    elif op == '^':
        data[coord] **= val
    elif op == '/':
        data[coord] /= val
    elif op == '%':
        data[coord] %= val
    elif op == '!':
        data[coord] = math.factorial(val)
    elif op[0] == '@':
        data[coord] = val**(1/int(op[1]))
def execute(code):
    global printing, print_list, num, looping
    num = -1
    while num < len(code) - 1:
        num += 1
        if printing == 0:
            if code[num][0] == '~':
                pass
            elif code[num][0] == 'PRINT':
                sep = code[num][2]
                printing = int(code[num][1])
            elif code[num][0] == 'LOOP':
                __init__LOOP(num, int(code[num][1]), int(code[num][2]))
            elif code[num][0] == 'VAR':
                VAR(code[num])
            elif code[num][0] == 'IF':
                IF(code[num])
            elif code[num][0] == 'INIT':
                INIT(code[num])
            else:
                pass
        elif printing == 1:
            print_list.append(code[num])
            printing -= 1
            PRINT(print_list, sep)
            print_list = []
        elif printing > 1:
            print_list.append(code[num])
            printing -= 1
        if looping:
            LOOP()
execute(code)
print('finished')
