def invert(l):
    if len(l) == 0: #Caso base
        return []
    if len(l) == 1:
        return l[::]
    else:
        return l[-1:] + invert(l[:-1]) #Passo recursivo


lista = [1, 2, 3, 4, 5]
print("lista inicial: ", lista)
print("lista invertida: ", invert(lista))
