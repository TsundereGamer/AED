class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.previous = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = self.length
        while current is not None:
            count = count + 1
            current = current.next

        return count

    def add(self, new_data):
        new_node = Node(data=new_data)

        new_node.next = self.head
        new_node.previous = None

        if self.head is not None:
            self.head.previous = new_node

        self.head = new_node

    def remove(self, item):
        if self.head is None:
            print("The list has no element to delete")
            return
        if self.head.next is None:
            if self.head.item == item:
                self.head = None
            else:
                print("Item not found")
            return

        if self.head.item == item:
            self.head = self.head.next
            self.head.previous = None
            return

        temp = self.head
        while temp.next is not None:
            if temp.item == item:
                break
            temp = temp.next
        if temp.next is not None:
            temp.previous.next = temp.next
            temp.next.previous = temp.previous
        else:
            if temp.item == item:
                temp.previous.next = None
            else:
                print("Element not found")

    def search(self, item):
        current = self.head
        index = 0
        while current is not None:
            if current.item == item:
                return index
            current = current.next
            index += 1
        return -1

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


d = DoubleLinkedList()
d.add(2)
d.add(10)
d.add(5)
d.add(15)
d.add(30)
d.add(40)
d.add(25)
d.add(12)
print("Lista inicial", d, "\n")

d.remove(5)
print("5 removido da Lista")
print("Lista", d, "\n")

d.remove(40)
print("40 removido da Lista")
print("Lista", d, "\n")

print("Nº 10 no indice", d.search(10))
print("Nº de items na Lista", d.size())
print("Lista está vazia?", d.isEmpty())


