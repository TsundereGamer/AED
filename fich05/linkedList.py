from fich05.ex01_node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
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
        try:
            if current is None:
                return

            while current.getData() == item:
                previous = current
                current = current.getNext
                if current is None:
                    return

            current = self.head
            while current.getNext is not None:
                if current.getData() == item:
                    previous = current
                    current = current.getNext
                else:
                    current = current.getNext
            return


            # if previous is None:
            #     self.head = current.getNext()
            # else:
            #     previous.setNext(current.getNext())

        except AttributeError:
            print(item, "Not in list. Cannot be removed!")

        # current = self.head
        # previous = None
        # try:
        #     while current is not None:
        #         if current.getData() == item:
        #             previous = current
        #             current = current.getNext()
        #         else:
        #
        #
        #     if previous is None:
        #         self.head = current.getNext()
        #     else:
        #         previous.setNext(current.getNext())
        #
        # except AttributeError:
        #     print(item, "Not in list. Cannot be removed!")

        # Lista Vazia; Nao ha trabalho a fazer
        # if self.head is None:
        #     return
        # # Remover todas as ocurencias do item a ser removido no cabeçalho
        # while self.head.getData() == item:
        #     # Remove o promixo Node
        #     self.head = self.head.getNext()
        #     if self.head is None:
        #         # Lista está agora vazia
        #         return
        #
        # # Remover ocurrencias adicionais do item
        # current = self.head
        # while current.getNext() is not None:
        #     if current.getNext().getData() == item:
        #         # Remover o proximo Node
        #         current.getNext = current.getNext().getNext()
        #     else:
        #         # Nao remover o proximo node; simplesmente avançar para proximo
        #         current = current.getNext
        # # Fim da lista ligada
        # return

    # def remove(self, item):
    #     current = self.head
    #     previous = None
    #     try:
    #         while current is not None:
    #             if current.getData() == item:
    #                 current.remove()
    #             else:
    #                 previous = current
    #                 current = current.getNext()
    #
    #         if previous is None:
    #             self.head = current.getNext()
    #         else:
    #             previous.setNext(current.getNext())
    #
    #     except AttributeError:
    #         print(item, "Not in list. Cannot be removed!")

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

