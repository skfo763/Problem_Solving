import sys
input = sys.stdin.readline
dwarf_list = []
seven_list = []

for i in range(9):
    dwarf_list.append(int(input().rstrip()))

for i in range(len(dwarf_list)):
    for j in range(i, len(dwarf_list)):
        available_dwarfs = []
        for k in range(len(dwarf_list)):
            if k != i and k != j:
                available_dwarfs.append(dwarf_list[k])
        seven_list.append(available_dwarfs)

result = []
for dwarfs in seven_list:
    if sum(dwarfs) == 100:
        result = sorted(dwarfs)

for height in result:
    print(height)