import sys
input = sys.stdin.readline

e, s, m = map(int, input().rstrip().split())
result = 1
curr_e, curr_s, curr_m = 1, 1, 1

while True:
    if curr_e == e and curr_s == s and curr_m == m:
        break
    curr_e = curr_e + 1 if curr_e + 1 <= 15 else 1
    curr_s = curr_s + 1 if curr_s + 1 <= 28 else 1
    curr_m = curr_m + 1 if curr_m + 1 <= 19 else 1
    result += 1

print(result)