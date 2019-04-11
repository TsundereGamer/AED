from fich03_group_I.stack import Stack
from fich03_group_I.ex05_declaracoes import infixToPostfix


def number(x):
    try:
        if isinstance(int(x), int):
            return True, int(x)
    except:
        try:
            if isinstance(float(x), float):
                return True, float(x)
        except:
            return False, None


def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:

        is_number, token_number = number(token)

        if is_number:
            operandStack.push(token_number)
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()

            result = doMath(token,operand1,operand2)

            operandStack.push(result)

    return operandStack.pop()


def doMath(op, op1, op2):
    if op == "^":
        return op1 ** op2
    elif op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


def main():
    postfixExpressions = ['4.4 4.6 + 2 1 3 + / ^', '2 20 ^ 2 1 3 + / ^', '2 20 + 2 1 3 + + *', '2 -1 3 + -']

    for expression in postfixExpressions:
        print(expression + " = " + str(postfixEval(expression)))

    infixExpressions = ["7 + 9 * 8 - 4 ^ 2", "7 + 9 * 8 / 4 ^ 2", "( 17 + 9 ) * 3 / ( 5 - 3 ) ^ 4",
                        "7.5 + 9 - 1.8 / 4 ^ 2.5"]

    for expression in infixExpressions:
        post = infixToPostfix(expression)
        print(expression + " = " + str(postfixEval(post)))


if __name__ == "__main__":
    main()