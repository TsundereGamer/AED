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

print("n         pop(0)     pop()")
for n in range(1000000,100000001,1000000):
    x = list(range(n))
    p_end = popend.timeit(number=1000)
    x = list(range(n))
    p_zero = popzero.timeit(number=1000)
    print(n, end="")
    print("%10.5f %10.5f" %(p_zero, p_end))