# The time  module allows you the measure times precisely and
# one of the advantage over the way we did time before
# is that it works consistently across different platforms whether
# you're in UNIX on a Mac or in Windows it gives you the same time
import timeit

def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))


# create Timer object, whose parameters are two strings.
# Each string should be a Python statement

#                                      |statement that run once before timing runs
#                                      |(this one imports the function test1
#                                      |from __main__ namespace into the namespace that timeit
#                 |statement to time   |runs the timing experiment)
t1 = timeit.Timer( "test1()",          "from __main__ import test1")

# We can pass to timeit a named parameter called number that
# allows to specify how many times the test statement is executed
print("concat ", t1.timeit(number=1000), "milliseconds")

t2 = timeit.Timer("test2()", "from __main__ import test2")
print("append ", t2.timeit(number=1000), "milliseconds")

t3 = timeit.Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000), "milliseconds")

t4 = timeit.Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "milliseconds")




