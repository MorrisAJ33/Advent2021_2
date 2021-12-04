file3 = open('D3_input.txt', 'r')
lines = file3.readlines()
oxygen = ''
C02 = ''
index = 0
for p in range(0, 12):
    print(f'p= {p}')
    print(lines)
    zeros = 0
    ones = 0
    if len(lines) > 2:
        for line in lines:
            if line[p] == '0':
                zeros += 1
            else:
                ones += 1
        if zeros < ones:
            oxygen = oxygen + '0'
        else:
            oxygen = oxygen + '1'
        print(f'zero = {zeros}  one = {ones}')
        dropper = oxygen[p]
        drops = []
        print(f'dropper value = {dropper}')
        lines_len = len(lines)
        print(f'{p} stage length = {lines_len}')
        for d in range(0, lines_len):
            # print(f'd= {d}')
            # print(f'line = {lines[d]}')
            if lines[d][p] == oxygen[p]:
                drops.insert(index, d)
                index += 1
        drops.reverse()
        print(f'dropping {p}')
        for i in drops:
            lines.pop(i)
        print(f'O2 current = {oxygen}')
    elif len(lines) <= 2:
        if lines[0][p] == '1':
            oxygen = lines[0]
        elif len(lines) == 2 and lines[1][p] == '1':
            oxygen = lines[1]
print(f'oxygen_string= {oxygen}')
oxygen = int(oxygen[:12], 2)
print(f'O2 number= {oxygen}')
file3_2 = open('D3_input.txt', 'r')
lines2 = file3_2.readlines()
for p in range(0, 12):
    print(f'p={p}')
    print(lines2)
    zeros = 0
    ones = 0
    if len(lines2) > 2:
        for line in lines2:
            if line[p] == '0':
                zeros += 1
            else:
                ones += 1
        if zeros > ones:
            C02 += '0'
        else:
            C02 += '1'
        print(f'zero = {zeros}  one = {ones}')
        dropper = C02[p]
        dropping = []
        index2 = 0
        print(f'dropper value = {dropper}')
        lines2_len = len(lines2)
        print(f'{p} stage length = {lines2_len}')
        for d in range(0, lines2_len):
            if lines2[d][p] == C02[p]:
                dropping.insert(index2, d)
                index2 += 1
        dropping.reverse()
        print(f'dropping {p}')
        for i in dropping:
            lines2.pop(i)
        print(f'CO2 current = {C02}')
    elif len(lines2) <= 2:
        if lines2[0][p] == '0':
            C02 = lines2[0]
        elif len(lines2) == 2 and lines2[1][p] == '0':
            C02 = lines2[1]
print(f'CO2 Final = {C02[:12]}')
C02 = int(C02[:11], 2)
print(f'C02 number = {C02}')
print(f'final = {oxygen * C02}')
