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

# myString = "The quick brown fox jumped over the lazy dog"
# myStringList = list(myString)
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
# myCars = ["ford", "toyota", "opel", "bmw", "mitsubshi", "chevrolet"]
# # declaring my input
# print("Enter a make of car")
# carName = input()
# if carName not in myCars:
#     print("We do not stock", carName)
# else:
#     print("Yes we do stock", carName)

# Appending an item to a list #

# unlike strings we can change individual items in a list 
# using indexing
# Lists are said to be "mutable" - this means individual items can be appended, removed or changed

# myList = [1, 19, 27, 5, 8, 9]

# # to add an item to a list we use the following:
# # .append()

# myList.append(11)
# print(myList)

# # Inserting an item to a list #
# # inserting an item is different than adding - we can pick where it goes

# # to insert an item to a list we use for following:
# # .insert()
# # this function however takes 2 arguments, not 1 argument like .append

# myList.insert(1, 13)
# print(myList)

# # the first argument gives the index of the inserted value
# # the second argument gives its value

# # removing an item from a list # 
# # to remove an item from a list we use the following:
# # .remove()

# myList.remove(myList[-1])
# print(myList)

# finding the location of am item im a list #
# to find the location of a certain value we can do the following:
# .index()

# myList = [1, 19, 27, 5, 8, 5, 9, 5]
# print(myList.index(5))

# even if there are multiple values, Python will only print
#out the first instance of the value it finds

# locating items that occur more than once in a list

# We can use while or for loops to find the number of times the value 5 occurs

# myList = [1, 19, 27, 5, 8, 5, 9, 5]
# numSought = 5 # the value i want
# freqNum = 0 # frequency to record each occurence of the number
# counter = 0 # counter to control the number of times my loop is executed

# while counter < len(myList):
#     if myList[counter] == numSought:
#         freqNum += 1
#         print("Found at index:", counter)
#     counter += 1
# print(freqNum)
# print(counter)

myList = []
for _ in range(5):
    myList.append(int(input("Input a number ")))
print(myList)

for x in range(len(myList)):
    myList[x] +=1
print(myList)
