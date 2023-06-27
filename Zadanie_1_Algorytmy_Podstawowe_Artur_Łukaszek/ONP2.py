inPut = "4 5 6 3 / - 1 + 2 ^ *"
outPut = [""]
stack = []
for element in inPut:
    if element != ' ':
        if element.isnumeric():
            stack.append(str(element))
        else:
            if len(stack) > 1:
                if element == '^':
                    result = f"({stack[-2]}){element} {stack[-1]}"
                else:
                    result = f"{stack[-2]} {element} {stack[-1]}"
                stack.pop()
                stack.pop()
                stack.append(result)

print(stack[0])