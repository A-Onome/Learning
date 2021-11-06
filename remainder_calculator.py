from math import *
value1 = input("Enter first number: ")
value2 = input("Enter second number: ")
result = int(value1) / int(value2)
result2 = int(value1) % int(value2)
if result2 == 0:
    print(floor(result))
else:
    print(str(floor(result))+" with a remainder of " +str(result2))
#testing to see if i can commit and push directly from pyCharm