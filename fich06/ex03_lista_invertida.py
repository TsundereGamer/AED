def invert(l):
    if not l:
        return l
    else:
        return l[-1:] + invert(l[:-1])


lista = [1, 2, 3, 4, 5]
print("lista inicial: ", lista)
print("lista invertida: ", invert(lista))
