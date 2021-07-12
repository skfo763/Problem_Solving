import copy

def f(numbers, count):
    if count == 1:
        res = []
        for item in numbers:
            res.append([item])
        return res

    res_list = []
    prev_res = f(numbers, count-1)
    for item in prev_res:
        for i in numbers:
            if item.__contains__(i):
                continue
            temp_item = copy.deepcopy(item)
            temp_item.append(i)
            res_list.append(temp_item)
    return res_list


input_numbers = list(map(int, input().split(' ')))
k = int(input())

result = -1
for combination in f(input_numbers, len(input_numbers)):
    is_sorted = True
    for i in range(0, len(combination)-1):
        if abs(combination[i] - combination[i+1]) > k:
            is_sorted = False

    if not is_sorted:
        continue

    modified = copy.deepcopy(combination)
    swap = 0
    for i in range(len(modified)):
        if modified[i] != input_numbers[i]:
            target = modified.index(input_numbers[i])
            swap += 1
            temp = modified[i]
            modified[i] = modified[target]
            modified[target] = temp
    result = swap if(result == -1) else min(swap, result)

print(result)








