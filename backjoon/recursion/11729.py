import sys
input = sys.stdin.readline
result = []


def hanoi_tower(plate, dep, arr, sub):
    global result
    if plate == 1:
        result.append(str(dep) + " " + str(arr))
        return
    hanoi_tower(plate-1, dep, sub, arr)
    result.append(str(dep) + " " + str(arr))
    hanoi_tower(plate-1, sub, arr, dep)


plate_count = int(input().rstrip())
hanoi_tower(plate_count, 1, 3, 2)
print(len(result))
for seq in result:
    print(seq)


