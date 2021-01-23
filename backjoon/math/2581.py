import sys
input = sys.stdin.readline


def get_checked_prime_number_list(size):
    is_prime_list = [True for _ in range(size + 1)]
    is_prime_list[0] = False
    is_prime_list[1] = False

    for i in range(2, int(size ** 0.5) + 1):
        if not is_prime_list[i]:
            continue
        for j in range(i, size // i + 1):
            is_prime_list[i * j] = False
    return is_prime_list


min = int(input())
max = int(input())
prime_number_list = get_checked_prime_number_list(10001)
result_sum = 0
result_min = -1

for i in range(min, max+1):
    if prime_number_list[i]:
        if result_min == -1:
            result_min = i
        result_sum += i

if result_sum > 0:
    print(result_sum)
    print(result_min)
else:
    print("-1")