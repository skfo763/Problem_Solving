word = input()
char_list = [0 for i in range(26)]

for char in word:
    index = ord(char) - ord('a')
    char_list[index] += 1

for count in char_list:
    print(count, end=' ')
