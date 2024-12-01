import postfix

def test():
    assert postfix.eval_expr("1 2 +") == 3
    assert postfix.eval_expr("1 2 -") == -1
    assert postfix.eval_expr("2 1 -") == 1
    assert postfix.eval_expr("2 2 + 3 *") == 12
    assert postfix.eval_expr("2 2 * 3 +") == 7
    assert postfix.eval_expr("2 2 3 * +") == 8
    assert postfix.eval_expr("10 2 /") == 5
    assert postfix.eval_expr("5 2 * 2 /") == 5
    assert postfix.eval_expr("5 2 /") == 2
    assert postfix.eval_expr("5 2 / 2 *") == 4

    print("Success!")