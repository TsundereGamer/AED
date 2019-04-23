def invert(txt):
    if len(txt) == 0:
        return txt
    else:
        return invert(txt[1:]) + txt[0]


string = input(str("Insira uma string"))
print(string)
print(invert(string))