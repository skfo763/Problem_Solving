def is_num(k, number):
    multi = round(k * number, 1)
    if int(multi) == multi:
        return True
    return False


n = int(input())
float_list = []
for i in range(n):
    float_list.append(float(input()))

answer = 1000
for k in range(1, 1001):
    flag = True
    for number in float_list:
        if is_num(k, number):
            flag = True
            continue
        flag = False
        break
    if flag:
        answer = k
        break
print(answer)



