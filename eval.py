def evaluate_expression(expr, stack):
    for e in expr:
        if e.isdigit():
            stack.append(int(e))
        elif e == "+":
            a = stack.pop()
            b = stack.pop()
            stack.append(a+b)
        elif e == "-":
            a = stack.pop()
            b = stack.pop()
            stack.append(a-b)
        elif e == "*":
            a = stack.pop()
            b = stack.pop()
            stack.append(a*b)
        elif e == "/":
            a = stack.pop()
            b = stack.pop()
            stack.append(a/b)


        elif e == "p":
            print(stack[-1])
            print(stack)
    pass

stack = []

while True:
    expr = input()
    expr =  expr.split()

    print()
    done = evaluate_expression(expr, stack)
    if done:
        break