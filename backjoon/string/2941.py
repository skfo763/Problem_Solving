convert_list = [
    "dz=",
    "z=",
    "s=",
    "nj",
    "lj",
    "d-",
    "c=",
    "c-"
]

word = input()

for index, croatian_letter in enumerate(convert_list):
    word = word.replace(croatian_letter, str(index))

print(len(word))
