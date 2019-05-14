class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped

    def peek(self):
        if self.head is None:
            return "Peek from empty stack."
        else:
            return self.head.data

    def isEmpty(self):
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
            result += str(current.data)
            current = current.next
            while current:
                result += ", " + str(current.data)
                current = current.next
        result += "]"
        return result


s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.push(60)
print("Stack inicial:", s)
print("Pop:", s.pop())
print("Pop:", s.pop(), "\n")

print("Stack:", s)
print("Nº de items: ", s.size())
print("Stack vazia?:", s.isEmpty())
print("Topo da stack:", s.peek())
print("Pop:", s.pop())
print("Pop:", s.pop())
print("Pop:", s.pop())
print("Pop:", s.pop())
print(s)
print("Pop:", s.pop())

