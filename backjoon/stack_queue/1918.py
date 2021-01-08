postfix_stack = []
infix = input()
res = ""

for c in infix:
    if c == '(':
        postfix_stack.append(c)
    elif c == ')':
        while postfix_stack and postfix_stack[-1] != '(':
            res += postfix_stack.pop()
        postfix_stack.pop()
    elif c == '*' or c == '/':
        while postfix_stack and (postfix_stack[-1] == '*' or postfix_stack[-1] == '/'):
            res += postfix_stack.pop()
        postfix_stack.append(c)
    elif c == "+" or c == '-':
        while postfix_stack and postfix_stack[-1] != '(':
            res += postfix_stack.pop()
        postfix_stack.append(c)
    else:
        res += c

while postfix_stack:
    res += postfix_stack.pop()

print(res)
