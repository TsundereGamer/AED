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

        if current is not None:
            if current.getData() == item:
                self.head = current.getNext()
                return

        while current is not None:
            if current.getData() == item:
                print('Item removido: ', current.getData())
                break
            previous = current
            current = current.getNext()

        try:
            previous.next = current.getNext()
        except:
            print('Item nao encontrado: ', item)

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
my_list.add(93)
my_list.add(26)
my_list.add(54)
my_list.add(17)
print("Lista inicial: ", my_list)
my_list.remove(5)
my_list.remove(54)
print("Lista depois: ", my_list)