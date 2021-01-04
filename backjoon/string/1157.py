word = input()
word = word.lower()
list = []

for i in range(0, 26):
    list.append(0)

for char in word:
    list[ord(char) - ord('a')] += 1

max_value = max(list)
max_char = ""

for index, value in enumerate(list):
    if value == max_value:
        if max_char == "":
            max_char = chr(index + ord('A'))
        else:
            max_char = "?"

print(max_char)
