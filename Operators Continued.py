## Operators Continued

#predict before you run

basePrice = 13 # variable created and assigned value of 13
topping = 3 # variable created and assigned value of 3
toppingCost = 1.5 # variable created and assigned value of 1.5
print(basePrice + topping * toppingCost)
#topping cost is multiplied by the topings
#this is then added to the base price

#predict what you think will happen
# ans: go through each line of code to explain it
# I predict the answer will be 4.5 + 13 = 17.5

## Type Conversion ##
# Changing from one data type to another

x = "100" # string
a = int(x) # changes to int

# input() - always gives back a string
# 
# name = input("What is your name?")
# print("Hello", name)
# 
# age = input("What is your age?") # will be a string
# print("Hello", name, "aged", age)
# 
# age1 = int(age) + 1
# print(age1)

numPizzas = int(input("How many pizzas?"))
totalCost = numPizzas * basePrice # totalCost type = int
# print("Your total cost is", str(totalCost)) # converted totalCost back to str

###### Page 16 - Augmented Assignment

# a shortcut for updating variables using its own current value:

# x += 1 -----> this is the exact same as writing x = x + 1
# this also works for -= *= /= //= etc

numPizzas += 2
totalCost = numPizzas * basePrice
print(totalCost, "is the total cost")