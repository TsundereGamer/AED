from fich03_group_I.stack import Stack


def is_float(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


def infixToPostfix(infixexpr):
    prec = {}
    prec["^"] = 3
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or is_float(token):
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                try:
                    topToken = opStack.pop()
                except IndexError:
                    return "Expressão Inválida: " + infixexpr
        else:
            try:
                while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                    postfixList.append(opStack.pop())
                opStack.push(token)
            except KeyError:
                return "Operador Inválido: " + infixexpr

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)


print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ^ ) * C - ( D - E ) * ( F + G )"))
print(infixToPostfix("1 * 2.5 + C * D"))
