from sys import stdin

n = int(stdin.readline())
input_data = []
for index in range(n):
    input_data.append(int(stdin.readline()))


def get_result():
    stack, result, count = [], [], 1

    for i in input_data:
        while count <= i:
            stack.append(count)
            result.append("+")
            count = count + 1
        if stack.pop() == i:
            result.append("-")
        else:
            return "NO"
    return "\n".join(result)


print(get_result())
