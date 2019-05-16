# The time  module allows you the measure times precisely and
# one of the advantage over the way we did time before
# is that it works consistently across different platforms whether
# you're in UNIX on a Mac or in Windows it gives you the same time
import timeit

# create Timer objects, whose parameters are two strings.
# Each string should be a Python statement
popzero = timeit.Timer( "x.pop(0)",                # statement to time
                        "from __main__ import x")  # statement that run once before timing runs
popend = timeit.Timer("x.pop()",
                      "from __main__ import x")

x = list(range(2000000))
print(popzero.timeit(number=1000))


x = list(range(2000000))
print(popend.timeit(number=1000))
