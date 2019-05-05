from fich05.ex01_node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.head is None

    def size(self):
        return str(self.size)

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        self.size += 1

    def remove(self, item):

        if self.head is None:
            return

        while self.head.data == item:
            self.head = self.head.next
            self.size -= 1
            if self.head is None:
                return

        current = self.head
        while current.next is not None:
            if current.next.data == item:
                current.next = current.next.next
                self.size -= 1
            else:
                current = current.next
        return

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
        current = self.head
        if current is not None:
            result += str(current.getData())
            current = current.getNext()
            while current:
                result += ", " + str(current.getData())
                current = current.getNext()
        result += "]"
        return result


my_list = LinkedList()
my_list.add(17)
my_list.add(17)
my_list.add(17)
my_list.add(26)
my_list.add(93)
my_list.add(26)
my_list.add(54)
my_list.add(17)
print("Lista inicial: ", my_list)
print("Nº Elementos: ", my_list.size)
my_list.remove(17)
print("Lista depois: ", my_list)
print("Nº Elementos: ", my_list.size)