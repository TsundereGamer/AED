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


def main():
    print(infixToPostfix("A * B + C ^ D"))
    print(infixToPostfix("( 4.4 + 4.6 ) ^ ( 2 / ( 1 + 3 ) )"))
    print(infixToPostfix("( 2 ^ 20 ) ^ ( 2 / ( 1 + 3 ) )"))
    print(infixToPostfix("A * B ) + ( C ^ D )"))
    print(infixToPostfix("( A * B ) + (C ^ D )"))
    print(infixToPostfix("7 + 9 * 8 / 4 ^ 2"))
    print(infixToPostfix("( 17 + 9 ) * 3 / ( 5 - 3 ) ^ 4"))


if __name__ == "__main__":
    main()
