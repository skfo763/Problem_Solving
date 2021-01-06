people_count, distance = list(map(int, input().split()))
circular_list = [i + 1 for i in range(people_count)]
result = []
delete_index = 0

for i in range(len(circular_list)):
    delete_index = (delete_index + distance - 1) % len(circular_list)
    result.append(str(circular_list.pop(delete_index)))

print("<%s>" % (", ".join(result)))
