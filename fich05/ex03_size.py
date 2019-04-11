from fich05.ex01_node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = self.length
        while current is not None:
            count = count + 1
            current = current.getNext()

        return count

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def __str__(self):
        result = "["
        node = self.head
        if node is not None:
            result += str(node.data)
            node = node.next
            while node:
                result += ", " + str(node.data)
                node = node.next
        result += "]"
        return result