import sys

input = sys.stdin.readline
a, b, c = map(int, input().rstrip().split())

first_value = (a + b) % c
second_value = ((a % c) + (b % c)) % c

third_value = (a * b) % c
fourth_value = ((a % c) * (b % c)) % c

print(first_value)
print(second_value)
print(third_value)
print(fourth_value)
