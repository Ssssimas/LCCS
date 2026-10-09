## Selection intro ##

#Prorams often need to branch off in different
# directions depending on certain conditions

# these are called either selections or conditionals

# conditionals use boolean expressions to test if something is
# true of false
# depending on the result of the test. a different branch
# is taken through the pathway

# Python ises a colon (:) amd INDENTATION to show which lines
# of code are inside of our conditional

## one branch is an if statement ##

# the simplest type of conditional
# if the condition is true - computer executes the code
# if the condition is not true, the code is skipped
# net statement is executed

# answer = input("Do you have a loyalty card? (Y/N)").upper() # asks if the user has a loyalty card then sets the input to uppercase
# if answer == "Y": # if the input is Y
#     print("Please scan your card") # prints please scan your card
# 
# answer = input("Do you have a loyalty card? (Y/N)").upper() 		# asks if the user has a loyalty card then sets the input to uppercase
# if answer == "Y": 													# if the input is Y
#     print("Please scan your card")									# prints please scan your card
# else: 																# if the answer is not Y
#     if answer == "N":												# it checks if the answer is N, if it is it
#         SignUp = input("Would you like to sign up? (Y/N)").upper()  # asks if the user wants to sign up
#         if SignUp == "Y":											# if the user wants to sign up
#             print("Signup")											# it prints signup
#             
#             
            
## Elif Statement ##

# payType = input("Do you want to pay by cash, card or voucher?").lower()
# if payType == "cash":
#     print("please insert cash")
# elif payType == "card":
#     print("Please insert your card now")
# elif payType == "voucher":
#     print("Please scan your voucher now")
    
## homework - short class test tomorrow on
    #data types
    #operations
    #strings
    #computational thinking
    #variables


## elif is only checked if everything ABOVE it is falce,
# python stops at the very first true condition
# only one branch of an if/elif/else chain ever runs
# If there's nothing else at the bottom and nothing matches
# the program does nothing - no error


# task 1
# 
# lightColour = "red"
# 
# if lightColour == "red":
#     print("Stop")
# elif lightColour == "amber":
#     print("Get ready")
# elif lightColour == "green":
#     print("Go")
#     
#     
# ###########################
#     
# lightColour = "amber"
# 
# if lightColour == "red":
#     print("Stop")
# elif lightColour == "amber":
#     print("Get ready")
# elif lightColour == "green":
#     print("Go")
#     
#     
# ###########################
#     
#     
# lightColour = "green"
# 
# if lightColour == "red":
#     print("Stop")
# elif lightColour == "amber":
#     print("Get ready")
# elif lightColour == "green":
#     print("Go")
# 
# 


# Task 2

grade = int(input("What is your percentage grade?"))
level = str(input("What is your level? (HL/OL)")[0].upper())

if grade >= 90:
    print(level + "1")
elif grade >=80:
    print(level + "2")
elif grade >=70:
    print(level + "3")
elif grade >=60:
    print(level + "4")
elif grade >=50:
    print(level + "5")
elif grade >=40:
    print(level + "6")
elif grade >=30:
    print(level + "7")
elif grade >=0:
    print(level + "8")


