def get_left_index(data, curr, dist):
    return (curr + dist) % len(data)


people_count, distance = list(map(int, input().split()))
circular_list = [i + 1 for i in range(people_count)]
curr_index = 0
delete_index = distance - 1
result = []

for i in range(len(circular_list)):
    if i == 0:
        item = circular_list.pop(delete_index)
        curr_index = delete_index
    else:
        item = circular_list.pop(get_left_index(circular_list, curr_index, delete_index))
        curr_index = delete_index - 1
    result.append(item)


print(result)
