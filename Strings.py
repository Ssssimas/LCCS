## Strings

# A string is a sequence of characters
# each character has a position
# the position of a character is called an index
# counting starts at 0

#classwork program
firstName = "Simas"
lastName = "Rinkevicius"
FullName = firstName + " " + lastName

print ((FullName + " ")* 3)
# using + -----> concatenation
# * repeats a string many times (replication)



## Which letter is where - Indexing ##

# Python gives each elements/character an index starting at 0
# This allows Python to retrieve and work with each item
# seperately

#to use string indexing to take out a sigle item we use square brackets []
# and the index number, after the variable name

print(FullName[0])
print(FullName[-1])
print(FullName[5])
print(FullName[-6])
print(FullName[7])


## Substring ##

# sections of a string are called substrings, or slices
#they are indexed similarly using []
#but they have a starting point and an end point
# e.g. [6:10]
#this referes to the index numbers 6,7,8,9
# 10 is not included

print(FullName[0:17])

# [Start:End] pulls out a chunk of a string - the end position is not included
#leaving one side blank means to the start or to the end

# string methods: .upper() and .lower() ##

# .upper() --> TO UPPER CASE
# .lower() --> to lower case

print(FullName.upper())
print(FullName.lower())

## .upper() and .lower() dont chanve the variable itself
# it just hands back a new string
#the only way to change the variable is to use =
# i.e. Reassign it

## Measuring a string ##
# to find out the length of a string we use len()
# we can then use .find() to find out the indexof a certain character

print(len(FullName))
print(FullName.find(" "))

# .find() gives back -1 if it cant find what you're lookng for
# this shows up in exam questions


