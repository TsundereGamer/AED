import random

# name = "John Smith"
# age = 20
# is_new = True
#
# print("Patients data")
# print("| Name       | Age | New Patient |")
# print("| " + name + " | " + str(age) + "  | " + str(is_new) + "        |\n")

# name = input("What is your name?")
# color = input("What is your favourite color?")
# print(name + " likes " + color)

# house_price = 1000000
# has_good_credit = True
#
# if has_good_credit:
#     down_payment = 0.1 * house_price
# else:
#     down_payment = 0.2 * house_price
# print("Down payment: €" + str(down_payment))
# print(f"Down payment: €{down_payment}")

# text = ""
# while True:
#     text = input("").lower()
#
#     if text == "help":
#         print("""
# start - to start the car
# stop - to stop the car
# quit - to exit\n""")
#
#     elif text == "start":
#         print("Car started...Ready to go!\n")
#
#     elif text == "stop":
#         print("Car stopped.\n")
#
#     elif text == "quit":
#         print("Program ended.")
#         break

# prices = [10, 20, 30]
#
# total = 0
# for price in prices:
#     total = total + price
#
# print(f"The total is: €{total}")

# numbers = [5, 2, 5, 2, 2]

# for number in numbers:
#     for i in range(number):
#         print("x", end="")
#     print()

# for x_counter in numbers:
#     output = ''
#     for i in range(x_counter):
#         output = output + 'x'
#     print(output)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# mylist = [random.randrange(1, 21) for i in range(21)]

# print(f"{mylist}\n")
#
# max_num = mylist[0]
# for number in mylist:
#     if number > max_num:
#         max_num = number
# print(f"max num: {max_num}")

# mylist = [random.randrange(1, 21) for i in range(21)]
# print(f"{mylist}\n")
#
# uniques = []
#
# for number in mylist:
#     if number not in uniques:
#         uniques.append()
# print(f"{uniques}\n")

# mylist = [1, 2, 3, 4, 5]
#
# print("".join(str(mylist)))

# class Stack:
#     def __init__(self):
#         self.items = []
#
#     def isEmpty(self):
#         return self.items == []
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         return self.items.pop()
#
#     def peek(self):
#         return self.items[len(self.items) - 1]
#
#     def size(self):
#         return len(self.items)
#
# def main():
#     s = Stack()
#     print(s.isEmpty())
#     s.push(1)
#     s.push(12)
#     s.push(2)
#     s.push(13)
#     print(s.isEmpty())
#     s.pop()
#     print(f"Top item: {s.peek()}")
#     print(f"Size: {s.size()}")
#     print(s)
#
#
# if __name__ == '__main__':
#     main()

# def factorial_iter(n):
#     prod = 1
#     for i in range(1, n+1):
#         prod *= i
#     return prod
#
#
# print(factorial_iter(3))

# from random import randint
# l = []
# for i in range(10):
#     value = randint(1, 10)
#     l.append(value)
# print(l)

from fich03_group_I.stack import Stack


class Queue:
    def __init__(self):
        self.input = Stack()
        self.output = Stack()

    def isEmpty(self):
        return self.input.isEmpty() and self.output.isEmpty()

    def enqueue(self, item):
        self.input.push(item)

    def dequeue(self):
        for item in self.input.items:
            self.output.push(item)
        return self.output.pop()

    def size(self):
        return len(self.input.items)

    def __str__(self):
        string = ""
        for item in self.input.items:
            string = string + " " + str(item)

        return string

