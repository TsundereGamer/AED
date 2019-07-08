list = [i for i in range(1,11)]

print("list:", list)

start = int(input("Where to start: "))

sum = 0
for j in range(list[start], len(list)+1):
    sum = sum + j

print(sum)


# a_list = "10 5 3 50 4 45 30 2"
# j = eval(input("Insert where to start at"))
#
# sum = 0
# for i in range(a_list[j],len(a_list)):
#     sum = sum + i
#
# print(sum)