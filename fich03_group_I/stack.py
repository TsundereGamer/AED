class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def __str__(self):
        string = ""
        for item in self.items:
            string = string + " " + item

        return string


def main():
    s = Stack()

    s.push("a")
    s.push("b")
    s.push("c")
    s.push("d")
    s.push("e")
    s.push("f")
    print(s.peek())

    print(s)


if __name__ == "__main__":
        main()