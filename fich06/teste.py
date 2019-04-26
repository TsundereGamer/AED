def cycle(a):
    if a < 1:
        return a
    return str(cycle(a-1))


for i in cycle(10):
    print(i)
