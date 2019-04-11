class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, item):
        if isinstance(item, Node):
            if self.head is None:
                self.head = item
                item.previous = None
                item.next = None
                self.tail = item
            else:
                self.tail.next = item
                item.previous = self.tail
                self.tail = item
        return

    def output_list(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
        return


d = DoubleLinkedList()
d.add(2)
d.add(10)
d.add(5)
d.add(15)
d.output_list()


