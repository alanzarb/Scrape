# fib.py
""" Fibonacci series    """

import functools
import sys

# def main():
""" Grabbing command line parameters.
    Now figure out how to pass them to the vscode launch configuration
"""

#     for arg in sys.argv[1:]:
#         print(f"AAAArg: {arg} Type: {type(arg)}")
#         print("calling fib on " + arg)

#         fib(int(arg))
#         print("after calling fib")


@functools.lru_cache(maxsize=None)
def fib(num):
    if num < 2: return num
    else:
        return fib(num - 1) + fib(num - 2)


print("hello world")

if __name__ == "__main__":
    for n in range(1, 100):
        print(f"\nFib {n} is {fib(n)}".format(n))
