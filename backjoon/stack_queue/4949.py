import sys

input = sys.stdin.readline
left_braket = ['(', '[']
right_braket = [')', ']']


def is_match_braket(left, right):
    return (left == left_braket[0] and right == right_braket[0]) or (
                left == left_braket[1] and right == right_braket[1])


def braket_match(str):
    stack = []
    for char in str:
        if left_braket.__contains__(char) or right_braket.__contains__(char):
            if len(stack) > 0 and is_match_braket(stack[-1], char):
                stack.pop()
            else:
                stack.append(char)
        else:
            continue
    if len(stack) == 0:
        return "yes"
    else:
        return "no"


while True:
    sentence = input().strip('\n')
    if sentence == ".":
        break
    else:
        print(braket_match(sentence))