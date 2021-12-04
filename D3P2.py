file3 = open('D3_input.txt', 'r')
lines = file3.readlines()
oxygen = ''
C02 = ''
for p in range(0, 12):
    print(f'p= {p}')
    zeros = 0
    ones = 0
    for line in lines:
        if line[p] == '0':
            zeros += 1
        else:
            ones += 1
        if zeros > ones:
            oxygen = oxygen + '0'
        else:
            oxygen = oxygen + '1'
    dropper = oxygen[p]
    drops = []
    print(f'dropper value = {dropper}')
    lines_len = len(lines)
    print(f'{p} stage length = {lines_len}')
    for d in range(0, lines_len - 1):
        print(f'd= {d}')
        print(f'line = {lines[d]}')
        if lines_len == 2:
            if lines[d][p] == '1':
                oxygen = lines[d]
                print(f'oxygen = {oxygen}')
        elif lines[d][p] != oxygen[p]:
            drops.append[d]
            print('dropped')
        dropping = drops.reverse()
        for i in dropping:
            lines.pop(i)
oxygen = int(oxygen, 2)
file3_2 = open('D3_input.txt', 'r')
lines2 = file3_2.readlines()
for p in range(0, 12):
    zeros = 0
    ones = 0
    for line in lines2:
        if line[p] == '0':
            zeros += 1
        else:
            ones += 1
        if zeros < ones:
            C02 += '0'
        else:
            C02 += '1'
    dropper = C02[p]
    print(f'dropper value = {dropper}')
    lines2_len = len(lines2)
    print(f'{p} stage length = {lines2_len}')
    for d in range(0, lines2_len) :
        if lines2_len == 2:
            if lines[d][p] == '1':
                C02 = lines2[d]
                print(f'C02 = {C02}')
        elif lines[d][p] != C02[p]:
            lines.pop(d)
C02 = int(C02, 2)
print(f'final = {oxygen * C02}')