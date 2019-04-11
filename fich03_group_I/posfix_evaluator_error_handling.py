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
            try:
                operand2 = operandStack.pop()
                operand1 = operandStack.pop()
            except IndexError:
                print(postfixExpr + ": " + "Bad Expression")
                return

            result = doMath(token,operand1,operand2)
            if result is not None:
                operandStack.push(result)
            else:
                print(postfixExpr + ": " + "Bad Expression")
                return

    return operandStack.pop()


def doMath(op, op1, op2):
    if op == "^":
        return op1 ** op2
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    else:
        return None


def main():

    postfixExpressions = ['4.4 4.6 + 2 1 3 + / ^', '2 20 ^ 2 1 3 + / ^', '2 20 + 2 1 3 + + *', '2 -1 3 + -']

    for expression in postfixExpressions:
        print(expression + " = " + str(postfixEval(expression)))

    postfixExpressions = ['+', '3 +', ' 3 ++ 2', '2 4*', '3 2 + 2 4*']

    for expression in postfixExpressions:
        if(postfixEval(expression)):
            print(expression + " = " + str(postfixEval(expression)))


if __name__ == "__main__":
    main()

