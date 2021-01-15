import math


def is_prime_number(num):
    if num == 1:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


count = int(input())
arr = map(int, input().split())
result = 0

for number in arr:
    if is_prime_number(number):
        result += 1
    else:
        continue

print(result)
