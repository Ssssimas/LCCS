# ## last lesson:
# favNum = "7" # assigned variable favNum the value of 7
# # value assigned to favNum is a string
# favNum = favNum + 1 # wont work because variable value is a str
# print(favNum)
# # Pythin's arithmetic Operators
# 
# + # plus - additon
# - # minus - subtraction
# * # multiplication
# / # division
# 
# // # floor division
# # division that throws away the remainder
# 
# %
# # modulus
# # division that only gives you the remainder
# 
# **
# # exponent (to the power of) **2 / **3 / **4
# 
# ##order of opertations
# # B
# # E
# # M
# # D
# # A
# # S
# 
# #splitting the bill

friends = 3

#cost of each pizza
pizza1 = 12
pizza2 = 14.50
pizza3 = 17

#total cost of all pizzas
TotalPizzaBill = pizza1 + pizza2 + pizza3

splitPrice = TotalPizzaBill / friends

print(friends, "Friends")
print(splitPrice, "Each for Pizzas" )

side1 = 2
side2 = 3
side3 = 5
totalSides = side1 + side2 + side3
print("total cost for sides is", totalSides, "or split evenly it is", totalSides / friends )

MealTotal = totalSides + TotalPizzaBill
print(MealTotal, "Is the total cost of the meal and split evenly it is", MealTotal / friends)
