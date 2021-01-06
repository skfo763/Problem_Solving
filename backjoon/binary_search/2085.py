tree_count, target_length = map(int, input().split())
tree_list = list(map(int, input().split()))
low, high = 1, max(tree_list)

while low <= high:
    mid = (low + high) // 2
    result = 0
    for length in tree_list:
        result += length - mid if length - mid > 0 else 0

    if result >= target_length:
        low = mid + 1
    else:
        high = mid - 1

print(high)

