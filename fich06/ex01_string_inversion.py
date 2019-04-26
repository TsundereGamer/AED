def invert(s):
    if len(s) == 0:
        return s
    else:
        return invert(s[1:]) + s[0]


string = input(str("Insira uma string"))
print(string)
print(invert(string))