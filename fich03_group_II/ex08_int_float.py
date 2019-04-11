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
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


print(postfixEval('7 8 + 3 2 + /'))
print(postfixEval('4.4 4.6 + 2 1 3 + / ^'))
