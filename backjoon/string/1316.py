count = int(input())
result = 0


def is_group_word(word):
    char_stack = [word[0]]
    for i in range(1, len(word)):
        if word[i] == char_stack[-1]:
            continue
        else:
            char_stack.append(word[i])

    if len(set(char_stack)) == len(char_stack):
        return 1
    else:
        return 0


for i in range(0, count):
    word = input()
    result += is_group_word(word)

print(result)
