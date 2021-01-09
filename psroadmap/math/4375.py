import sys
# 1 = 4 * x        -> 1 / 4 = x        -> 1 % 4 = 0
# 11 = 4 * x       -> 11 / 4 = x       -> 11 % 4 = 0
# 111 = 4 * x      -> 111 / 4 = x      -> 111 % 4 = 0
# 1111 = 4 * x     -> 1111 / 4 = x     -> 1111 % 4 = 0
# 11111 = 4 * x    -> 11111 / 4 = x    -> 11111 % 4 = 0
# 111111 = 4 * x   -> 111111 / 4 = x   -> 111111 % 4 = 0
# ...
def get_one_number(input_number):
    count = 1
    number = 1
    while True:
        if number % input_number == 0:
            print(count)
            break
        else:
            number = number + (10 ** count)
            count += 1


for line in sys.stdin:
    if line:
        num = int(line)
        get_one_number(num)
    else:
        break
