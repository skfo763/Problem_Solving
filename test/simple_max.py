count = int(input())
px = [int(input()) for i in range(count)]

"""
result = 0

for i in range(len(px)):
    for j in range(i):
        minus = px[i] - px[j]
        if minus >= 0 and minus > result:
            result = minus

print(result)
"""

temp_min = px[0]
temp_max = px[0]
result = -1

for i in px:
    if temp_min > i:
        temp_min = i
    if temp_max < i:
        temp_max = i
        result = temp_max - temp_min

if temp_min == temp_max:
    print(0)
else:
    print(result)