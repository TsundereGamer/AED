class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __str__(self):
        string = ""

        n = self.size()-1

        while n >= 0:
            string = string + str(self.items[n]) + " "
            n = n - 1

        return string


def main():
    q = Queue()

    q.enqueue('a')
    q.enqueue('b')
    q.enqueue('c')
    q.enqueue('d')
    q.enqueue('e')
    q.enqueue('f')

    print(q)


if __name__ == "__main__":
    main()



