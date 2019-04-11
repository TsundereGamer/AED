from fich03_group_I.stack import Stack
from fich03_group_I.infix_to_postfix import infixToPostfix


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
        
        if token in number(token):
            operandStack.push(token)
        else:
            try:
                operand2 = operandStack.pop()
                operand1 = operandStack.pop()
            except IndexError:
                print(postfixExpr + ": Bad Expression")
                return
            
            result = doMath(token,operand1,operand2)
            if result is not None:
                operandStack.push(result)
            else:
                print(postfixExpr + ": " + "Bad Expression")
                return
            
    return operandStack.pop()


def doMath(op, op1, op2):
    #====Ex 09====
    if op == "^":
        return op1 ** op2
    #============
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


def main():
    postfixExpressions = ['4.4 4.6 + 2 1 3 + / ^', '2 20 ^ 2 1 3 + / ^', '2 20 + 2 1 3 + + *', '2 -1 3 + -']
    # infix = "( 4.4 + 4.6 ) * ( 2 ^ / ( 1 + 3 ) )"
    # print("Infix: " + infix)
    # post = infixToPostfix(infix)
    # print("Postfix: " + post)
    # postEval = postfixEval(post)
    # print("Eval: " + postEval)

if __name__ == "__main__":
    main()

