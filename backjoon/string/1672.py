import sys

input = sys.stdin.readline

dna_dict = {
    "A": 0,
    "G": 1,
    "C": 2,
    "T": 3
}

dna_combination = [
    [0, 2, 0, 1],
    [2, 1, 3, 0],
    [0, 3, 2, 1],
    [1, 0, 1, 3]
]

count = int(input().rstrip())
dna_array = input().rstrip()
curr_dna = -1

for dna in reversed(dna_array):
    if curr_dna == -1:
        curr_dna = dna_dict[dna]
    else:
        curr_dna = dna_combination[curr_dna][dna_dict[dna]]

for key, value in dna_dict.items():
    if value == curr_dna:
        print(key)
        break
