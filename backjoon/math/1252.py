import sys

input = sys.stdin.readline

first_num, second_num = input().rstrip().split()
first_num = list(first_num)
second_num = list(second_num)

if len(first_num) > len(second_num):
    for i in range(len(first_num) - len(second_num)):
        second_num.insert(0, '0')
else:
    for i in range(len(second_num) - len(first_num)):
        first_num.insert(0, '0')

reminder = 0
result = []

for i in range(len(first_num) - 1, -1, -1):
    addition = int(first_num[i]) + int(second_num[i]) + reminder
    reminder = addition // 2
    result.append(addition % 2)

if reminder != 0:
    result.append(reminder)

first_one = False
is_valid = False

for i in reversed(result):
    if i == 0 and not first_one:
        continue
    if i == 1 and not first_one:
        first_one = True
    is_valid = True
    print(i, end="")

if not is_valid:
    print(0)
