""" Explore f strings and formatting """
v = "VVVV"
""" PLAIN STRINGS WITH PARAMETERS"""
print("FIRST FIRST v: {0}, fmt1: {1}".format(908, 'vvv'))
print("SECOND v:{v} positional:{0}".format(2567, v='vlvlv'))
b = 567765
""" F STRINGS """
print(f"THIRD v:{v} positional:{b}")
aa = "STUFF"
print(aa.format(234, v="NEWV"))
print(aa)
bb = aa.format(234)
print("BB: " + bb)
print("aa: " + aa + " bb:" + bb)

#print(aa.format("ZERO", v="VVVV"))

from fib import fib
for nf in range(10, 14):
    print(f"Fib of {nf} is {fib(nf)}")
