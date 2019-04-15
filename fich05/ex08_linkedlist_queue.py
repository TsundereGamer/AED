class Node:
    def __init__(self, data=None, next=None):
        self.item = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_node):
        self.next = new_node


class Queue:
    def __init__(self, head=None):
        self.head = head

    def enqueue(self, data):
        new_item = Node(data)
        current = self.head
        if current is None:
            self.head = new_item
        else:
            while current.get_next():
                current = current.get_next()
            current.set_next(new_item)

    def dequeue(self):
        current = self.head
        if current is not None:
            self.head = current.get_next()
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
            result += str(current.item)
            current = current.next
            while current:
                result += ", " + str(current.item)
                current = current.next
        result += "]"
        return result


q = Queue()

q.enqueue("01")
q.enqueue("02")
q.enqueue("03")
q.enqueue("04")
q.enqueue("05")
print(q)
q.dequeue()
print(q)
q.dequeue()
print(q)
print(q.is_empty())
print(q.size())
# print(q.is_empty())
