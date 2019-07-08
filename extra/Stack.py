from time_complexity import LinkedList


class Stack:
    def __init__(self):
        self.items = LinkedList.LinkedList()   # items is a linked list

    def isEmpty(self):
        return self.items.isEmpty()

    def push(self, item):
        self.items.add(item)

    def pop(self):
        if self.isEmpty():
            print("The stack is empty.")
            return
        else:
            return self.items.pop(0)

    def peek(self):
        return self.items.getItem(0)

    def size(self):
        return self.items.size()

    def __repr__(self):
        if self.isEmpty():
            return "==="
        else:
            rep = ""
            current = self.items.head
            while current is not None:
                rep = rep + str(current.getData()) + "\n"
                current = current.getNext()
            rep = rep + "==="
            return rep


def test_stack():
    print("CREATING EMPTY STACK")
    s = Stack()
    print(s, "\n")
    print("The stack is empty?", s.isEmpty())
    print("Stack size:", s.size())

    push_items = [1, 2, 'dog', 4, 5]
    print("\nPUSHING ITEMS", push_items)
    for item in push_items:
        #print("Adding item", item, end="   ")
        s.push(item)
        #print("my_list =", my_list)

    print(s)
    print("The stack is empty?", s.isEmpty())
    print("Stack size:", s.size())
    print("Item on the top:", s.peek())

    print("\nPOPPING 2 ITEMS")
    s.pop()
    s.pop()
    print(s)
    print("The stack is empty?", s.isEmpty())
    print("Stack size:", s.size())
    print("Item on the top:", s.peek())

    item = 'cat'
    print("\nPUSHING ITEM", item)
    s.push(item)
    print(s)
    print("The stack is empty?", s.isEmpty())
    print("Stack size:", s.size())
    print("Item on the top:", s.peek())

    print("\nPOPPING ALL ITEMS")
    for i in range(s.size()):
        s.pop()

    print(s)
    print("The stack is empty?", s.isEmpty())
    print("Stack size:", s.size())


if __name__ == "__main__":
    test_stack()
