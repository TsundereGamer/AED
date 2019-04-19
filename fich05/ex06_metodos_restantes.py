from fich05.ex01_node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def remove(self, item):

        if self.head is None:
            return

        while self.head.data == item:
            self.head = self.head.next
            if self.head is None:
                return

        current = self.head
        while current.next is not None:
            if current.next.data == item:
                current.next = current.next.next
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

    def isEmpty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = self.length
        while current is not None:
            count = count + 1
            current = current.getNext()

        return count

    def append(self, item):
        current = self.head
        if current:
            while current.getNext() is not None:
                current = current.getNext()
            current.setNext(Node(item))
        else:
            self.head = Node(item)

    def index(self, item):
        pos = 0
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                pos += 1
        if not found:
            raise ValueError('Value not present in the List')
        return pos

    def insert(self, pos, item):
        node = Node(item)
        if not self.head:
            head = node
        elif pos == 0:
            node.next = self.head
            self.head = node
        else:
            previous = None
            current = self.head
            current_position = 0
            while (current_position < pos) and current.getNext():
                previous = current
                current = current.getNext()
                current_position += 1
            previous.next = node
            node.next = current
        return self.head

    def pop(self):
        current = self.head
        while current.getNext():
            if current.getNext() is None:
                return current
                del current
                break
            else:
                current = current.getNext()

    def pop(self, pos=None):
        if pos is None:
            pos = self.size()
        elif pos < 0 or pos >= self.size():
            raise ValueError("Position doesn't exist")

        current_pos = 0
        previous = None
        current = self.head
        while current.getNext() and current_pos < pos:
            previous = current
            current = current.getNext()
            current_pos += 1
        if previous is None:
            self.head = current.getNext()
        else:
            previous.next = current.getNext()
        return current.getData()

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
my_list.add(93)
my_list.add(26)
my_list.append(54)
my_list.append(17)
print("Popped item: ", my_list.pop())
print("Popped item: ", my_list.pop(1))
my_list.insert(3, 12)
my_list.insert(3, 11)
print("Index of ", 26, ":", my_list.index(26))
print("Lista: ", my_list)
