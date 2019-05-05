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
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
                self.size -= 1
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


def main():
    mylist = LinkedList()
    mylist.add(10)
    mylist.add(15)
    mylist.add(20)
    mylist.add(25)
    mylist.add(26)
    mylist.add(30)
    print("Lista:", mylist)
    print("Nº de Items:", mylist.size)
    mylist.remove(30)
    print("Lista:", mylist)
    print("Nº de Items:", mylist.size)


if __name__ == '__main__':
    main()
