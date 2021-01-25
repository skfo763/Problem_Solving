import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
vowel_list = ['a', 'e', 'i', 'o', 'u']


def get_available_set(input_data, k):
    if k == 1:
        return input_data
    else:
        prev_data = get_available_set(input_data, k - 1)
        res = []
        for prev_seq in prev_data:
            for curr in input_data:
                if prev_seq[-1] >= curr:
                    continue
                else:
                    res.append(prev_seq + curr)
        return res


def is_condition_ok(input_data):
    curr_vowel = 0
    curr_consonant = 0
    for char in input_data:
        if vowel_list.__contains__(char):
            curr_vowel += 1
        else:
            curr_consonant += 1
    return curr_vowel >= 1 and curr_consonant >= 2


a, b = map(int, input().rstrip().split())
data = input().rstrip().split()
data = sorted(data)

result = get_available_set(data, a)
result = set(result)
result = sorted(result)

for res_seq in result:
    if is_condition_ok(res_seq):
        print(res_seq)
