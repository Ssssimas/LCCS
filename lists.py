# lists #

# in Python we have another variable type called a list
# a list can be used to store a collection of data itmes, and to keep them in order if we want

# using lists means we dont have to code over and over again
# another name for a list is an "array"

# a list begins with a square bracket [
# the values inside a list are referred to as "items"
# items are separated by commas (,)
# strings in a list still have their quotation marks ["red"]
# a list closing with a square bracket ]

# myFirstList = ["red", "yellow", "pink", "green"]
# emptyList = []
# # an empty list is the simplest type of list
# # we can add items to it

# myString = "John Baker"
# print(myString)
# myStringList = list(myString)
# print(myStringList)
# # list() finction will take all characters in my string and convert them into individual items(that are still strings) and place them into the list

# print(type(myString))
# print(type(myStringList))
# # list is a new variable type we are looking at

# myList = [2, 3.0, "red"]

# Indexing List #
#Indexing through a list is very similar to how we index through a string 

myString = "The quick brown fox jumped over the lazy dog"
myStringList = list(myString)
# print(myStringList)

# print(myStringList[2])
# print(myStringList[7])
# print(myStringList[10])
# print(myStringList[16])
# square bracket with one number inside will print the character at that position

# print(myStringList[2:8])
# when we use :, python will read everything from the first number up to but not including the last number

# Task # use the above list and indexing methods to print out the following words:
# Jumped
# the quick brown fox
# lazy dog

# print(myStringList[20:26])
# print(myStringList[0:19])
# print(myStringList[36:44])

# using "in" and "not in" operators with lists # 

# use these to check whether an item is or not in a list

# example:
# if "a" in ["a", "e", "i", "o", "u",]:
#     print("It is in the list")

# evaluates to a Boolean value

# example 2:
myCars = ["ford", "toyota", "opel", "bmw", "mitsubshi", "chevrolet"]
# declaring my input
print("Enter a make of car")
carName = input()
if carName not in myCars:
    print("We do not stock", carName)
else:
    print("Yes we do stock", carName)