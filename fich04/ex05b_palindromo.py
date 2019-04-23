from fich04.ex04_deque import Deque


def palchecker(aString):
    aString = aString.replace(" ", "")
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    still_equal = True

    while chardeque.size() > 1 and still_equal:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            still_equal = False

    return still_equal


print(palchecker("lsdkjfskf"))
print(palchecker("radar"))
print(palchecker("I PREFER PI"))
