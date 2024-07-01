
import sys
import math

#Printing a list
print("\n")
print("Printing list:")
newList = [1,3,5,8,4,352,35]
for val in newList:
    print(val)

print("\n")
print("Printing a for loop indexed range")
#I am able to index a for loop within these specific boundaries:
for i in range(2, 10):
    print(i)


print("\n")
print("Printing integer max size")
#Math.inf integer:
print(sys.maxsize)

print("\n")
print("Printing integer max float")
#Math.inf float:
print(math.inf)


print("\n")
print("The equivalent of 'not' ")
# ! equivalent is not
newList2 = [1,2,3,4,5]
if (6 not in newList2):
    print("6 is not in the newlist 2")
else:
    print("My understanding of is not is wrong")


print("\n")
print("Appending a list to a set using update:")
numbers = set()
numbers.update(newList)
print(numbers)

print("\n")
print("looking up a set")
if 3 in numbers:
    print("3 is in numbers")
else:
    print("3 is not in numbers")

print("\n")
print("Iterating through a list while providing index:")
for i, num in enumerate(numbers):
    print(num + " this is concatenating" + i)