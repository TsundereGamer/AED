from fich05.ex01_node import Node


class Queue:
    def __init__(self):
        self.head = None

    def enqueue(self, data):
        new_item = Node(data)

        current = self.head
        if current is None:
            self.head = new_item
        else:
            while current.getNext():
                current = current.getNext()
            current.setNext(new_item)

    def dequeue(self):
        current = self.head
        if current is not None:
            self.head = current.getNext()
        else:
            print("Queue is empty.")

    def is_empty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.next

        return count

    def __str__(self):
        result = "["
        current = self.head
        if current is not None:
            result += str(current.data)
            current = current.next
            while current:
                result += ", " + str(current.data)
                current = current.next
        result += "]"
        return result


q = Queue()
q.enqueue("01")
q.enqueue("02")
q.enqueue("03")
q.enqueue("04")
q.enqueue("05")
print("Fila inicial", q, "\n")

q.dequeue()
print(q)
q.dequeue()
print(q, "\n")

print("Fila Vazia?", q.is_empty())
print("Nº de Items", q.size())
