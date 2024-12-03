import operator

oper_d={
        '+':operator.add,
        '-':operator.sub,
        '*':operator.mul,
        '/':operator.floordiv,
        }


def eval_expr(s,**var_d):
    stack=[]
    
    for item in s.split():
        if item in oper_d:
            a = stack.pop()
            b = stack.pop()
            stack.append(oper_d[item](a,b))
        elif item in var_d:
            stack.append(int(var_d[item]))
        else:
            stack.append(int(item))
    return stack.pop()

def eval_expr_f(s):
    stack=[]
    
    for item in s.split():
        if item in oper_d:
            a_f = stack.pop()
            b_f = stack.pop()
            def fun(**var_d):
                return oper_d[item](a_f(**var_d),b_f(**var_d))
            stack.append(fun)
        elif item.isdigit():
            value=int(item)
            def fun(**var_d):
                return value
            stack.append(fun)
        else:
            def fun(**var_d):
                value = var_d[item]
            stack.append(fun)
    return stack.pop()
