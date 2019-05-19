class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class LinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def __str__(self):  # return string with items
        current = self.head
        s = "["
        while current is not None:
            s = s + str(current.getData())
            current = current.getNext()
            if current:
                s = s + ", "
        return s + "]"

    def isEmpty(self):
        return self.head is None

    # def size(self):
    #     current = self.head
    #     count = 0
    #     while current != None:
    #         count = count + 1
    #         current = current.getNext()
    #
    #     return count

    def size(self):
        return self.length

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        self.length = self.length + 1

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

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

        self.length = self.length - 1

    def append(self, item):
        temp = Node(item)

        if self.head is None:
            self.head = temp
        else:
            current = self.head
            while current.getNext() is not None:
                current = current.getNext()

            current.setNext(temp)

    def index(self, item):
        current = self.head
        found = False
        pos = 0
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                pos = pos + 1

        return pos

    def insert(self, pos, item):
        current = self.head
        temp = Node(item)
        if pos == 0:
            self.add(item)
        elif pos == self.size():
            self.append(item)
        else:
            previous = None
            position = 0
            while position < pos:
                previous = current
                current = current.getNext()
                position += 1

            temp.setNext(current)
            previous.setNext(temp)

    def pop(self, pos=-1):
        # last item
        if pos == -1:
            pos = self.size() - 1

        if pos == 0:
            item = self.head.getData()
            self.remove(item)
        else:
            current = self.head
            position = 0
            while position < pos:
                current = current.getNext()
                position += 1
            item = current.getData()
            self.remove(item)

        return item

    def getItem(self, pos):

        if pos == 0:
            return self.head.getData()

        else:
            current = self.head
            position = 0
            while position < pos:
                current = current.getNext()
                position += 1

            return current.getData()


def main():
    my_list = LinkedList()
    print("new list")

    my_list.add(12)
    print("add 12")

    my_list.remove(12)
    print("remove 12")

    print("Lista: ", my_list)
    print("List empty:", my_list.isEmpty(), "\n")

    my_list.add(31)
    print("add 31")
    my_list.add(77)
    print("add 77")
    my_list.add(17)
    print("add 17")
    my_list.add(93)
    print("add 93")
    my_list.add(26)
    print("add 26")
    my_list.add(54)
    print("add 54")
    print("Lista:", my_list)
    print("List empty:", my_list.isEmpty(), "\n")

    item = 10
    found = my_list.search(item)
    if found:
        print(item, "is in the list\n")
    else:
        print(item, "is NOT in the list\n")

    print("Pop", my_list.pop())
    print("Lista", my_list, "\n")

    print("Pop pos 0:", my_list.pop(0))
    print("Lista:", my_list, "\n")

    print("Pop pos 2:", my_list.pop(2))
    print("Lista:", my_list, "\n")

    print("Pop pos 2:", my_list.pop(2))
    print("Lista:", my_list, "\n")

    my_list.pop()
    print("Pop")
    my_list.append(2)
    print("append 2")
    print("Lista:", my_list, "\n")

    my_list = LinkedList()
    print("new list")
    my_list.append(93)
    print("append 93")
    print("Lista:", my_list)
    my_list.pop()
    print("Pop")
    print("Lista:", my_list, "\n")

    my_list = LinkedList()
    print("new list")
    my_list.append(31)
    print("append 31")
    my_list.append(77)
    print("append 77")
    my_list.append(17)
    print("append 17")
    my_list.append(93)
    print("append 93")
    print("Lista:", my_list)

    my_list.add(2)
    print("add 2")
    print("Lista:", my_list, "\n")

    print("pos of 31:", my_list.index(31))
    print("pos of 93:", my_list.index(93))
    print("pos of 2:", my_list.index(2), "\n")

    my_list = LinkedList()
    print("new list")

    my_list.insert(0, 31)
    print("insert 31 at pos 0")
    print("Lista:", my_list, "\n")
    my_list.add(77)
    print("add 77")
    print("Lista:", my_list, "\n")
    my_list.insert(2, 17)
    print("insert 17 at pos 2")
    print("Lista:", my_list, "\n")
    my_list.insert(1, 17)
    print("insert 17 at pos 1")
    print("Lista:", my_list, "\n")
    my_list.add(17)
    print("add 17")
    my_list.add(93)
    print("add 93")
    my_list.add(26)
    print("add 26")
    my_list.add(54)
    print("add 54")
    print("Lista:", my_list)


if __name__ == "__main__":
    main()