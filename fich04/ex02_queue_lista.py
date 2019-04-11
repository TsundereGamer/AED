class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(len(self.items)-1, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q = Queue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')
q.enqueue('d')
q.enqueue('e')
q.enqueue('f')

for item in q.items:
    print(item)



