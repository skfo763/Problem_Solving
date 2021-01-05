from functools import reduce

k = int(input())
number_list = []

for i in range(0, k):
    number = int(input())
    if number > 0:
        number_list.append(number)
    elif len(number_list) > 0:
        number_list.pop()
    else:
        continue

if len(number_list) > 0:
    print(reduce(lambda curr, next: curr + next, number_list))
else:
    print(0)