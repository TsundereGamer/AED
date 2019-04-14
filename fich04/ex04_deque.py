class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def __str__(self):
        string = ""
        for item in self.items:
           string = string + " " + item

        return string


def main():
    q = Deque()

    q.addRear("a")
    q.addRear("b")
    q.addRear("c")
    q.addRear("d")
    q.addRear("e")
    q.addRear("f")

    print(q)


if __name__ == "__main__":
        main()