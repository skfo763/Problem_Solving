weight = int(input())

weight_list = [1]
char_list = [chr(ord('A')+i) for i in range(26)]
for i in range(1, 26):
    prev = weight_list[i - 1]
    weight_list.append(((i+1)*prev) + prev)

result = ""
while weight > 1:
    max_list = []
    for i in range(len(weight_list)):
        if weight - weight_list[i] > 0:
            max_list.append(i)
    max_index = max(max_list)
    weight -= weight_list[max_index]
    result += char_list[max_index]

print(str(list(reversed(result))))

