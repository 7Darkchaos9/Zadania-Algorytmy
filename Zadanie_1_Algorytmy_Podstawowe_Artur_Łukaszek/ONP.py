def priorytet(znak):
    if znak == "^":
        return 3
    elif znak in "*/":
        return 2
    elif znak in "+-":
        return 1
    else:
        return 0


def ONP(dzialanie):
    stack = []
    outPut = ""
    for y in dzialanie:
        if y in "(+-*/^)":
            if not stack or y == '(':
                stack.append(y)
            elif y == ')':
                while stack[-1] != '(':
                    outPut += " " + stack.pop()
                stack.pop()
            elif stack and priorytet(stack[-1]) < priorytet(y):
                stack.append(y)
            elif stack and priorytet(stack[-1]) >= priorytet(y):
                while priorytet(stack[-1]) >= priorytet(y):
                    outPut += " " + stack.pop()
                stack.append(y)
        else:
            outPut += y
    while stack:
        outPut += " " + stack.pop()
    return outPut


x = "4 * (5 - 6 / 3 + 1) ^ 2"
print(ONP(x))

