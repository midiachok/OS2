def eval_expr(s):
    items=s.split()
    stack=[]
    
    for item in items:
        if item in {"+","-","/","*"}:
            a = stack.pop()
            b = stack.pop()
            if item == "+":
                stack.append(a+b)
            elif item == "-":
                stack.append(b-a)
            elif item == "/":
                stack.append(b//a)
            elif item == "*":
                stack.append(a*b)
        else:
            stack.append(int(item))
    return stack[0]
