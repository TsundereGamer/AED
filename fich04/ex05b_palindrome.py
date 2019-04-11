from fich04.ex04_deque import Deque

def palchecker(aString):
    aString = aString.replace(" ", "")
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual


print(palchecker("lsdkjfskf"))
print(palchecker("radar"))
print(palchecker("I PREFER PI"))
