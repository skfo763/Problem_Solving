def get_prime_number_list(size):
    check_prime = [True] * (size + 1)
    check_prime[0] = False
    check_prime[1] = False
    for i in range(2, int(size ** 0.5) + 1):
        if not check_prime[i]:
            continue
        for j in range(2, size // i + 1):
            check_prime[i * j] = False
    return check_prime


import sys

input = sys.stdin.readline
prime_number_list = get_prime_number_list(1000000)
prime_number_list[2] = False

while True:
    number = int(input())
    if number == 0:
        break

    for i in range(3, len(prime_number_list)):
        if prime_number_list[i] and prime_number_list[number - i]:
            print("%d = %d + %d" % (number, i, number - i))
            break
