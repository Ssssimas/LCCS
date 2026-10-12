## Iterations - While Loops

# Iteration occurswhen we instruct the computer to carry out
# a task over and over again

# This piece of code is called a loop

# there are 2 types of loops - a While loop and a FOR loop

## While loops ##

# A while loops keeps repeating while a certain condition is true
# it will only stop the loop once the condition is false

# counter = 0 			# counter is set to 0
# while counter <7:		# repeats this if counter is less than 7
#     print(counter)		# prints current counter
#     counter += 1		# adds 1 to counter
# print("Loop Finished")	# prints loop finished

## Task: try and create a loop to display the values from 1 to 100

# value = 0
# while value < 100:
#     print (value)
#     value += 1
    
# structure a while loop #
# 1) a loop control variable (a counter) which must
# be created and assigned a value. (this is called initialising)
# 2) the word while
# 3) A boolean expression to state the condition
# 4) a colon (Like if statements)
# 5) Inside the loop must begin with an indent
# 6) A way of changing the loop control variable
#   e.g. a counter in our example eventiually becomes false

# other use of while loops #

# a user is asked to enter an exam mark
# the exam mark must fall between 0 and 100
# while the mark entered falls outside the permissible range
# the user should be asked to re-endter the mark until it is inside the range


# mark = float(input("Enter an exam mark between 0 and 100: ")) # assigns the variable mark to an input of a float from the user

# while mark < 0 or mark > 100: # setting up a while loop with 2 conditions
#     print("Error Mark is outside range") # prints an error
#     mark = float(input("Re-enter a correct number")) # asks user to input a correct number

# print("You entered:", mark, " - well done!") # tells the user what numer they input and says well dones#


# in the following example we will display a menu that gives the user a user an option
# and keeps looping until the exit option is entered





# print("1 - Calculate the area of a circle") # explains what option 1 does
# print("2 - Calculate the volume of a sphere") # explains what option 2 does
# print("3 - Exit menu") # explains what option 3 does

# option = int(input("Enter option (1-3): ")) # takes an input from the user

# while (option != 3):    # while option isnt 3
#     if option == 1:     # if option is 1
#         r = float(input("Enter radius: "))  #asks user to input the radius, then sets it to a float
#         area = 3.14*(r**2)  # defines area variable
#         print("The area is: ", area)    # tells the user what the area variable is
#         option = 0  # resets option to 0 to allow the user to pick another option
#     elif option == 2:   # if option is 1
#         r = float(input("Enter the radius: "))  #asks user to input the radius, then sets it to a float
#         vol = (4/3) * (3.14 * (r**3))   # defines vol variable
#         print("The volume is: ", vol)   # tells the user what the area variable is
#         option = 0 # resets our variable
#     else:
#         print("Invalid option") # tells the user the option they input is invalid
#     #tells the user the options again
#     print("1 - Calculate the area of a circle")
#     print("2 - Calculate the volume of a sphere")
#     print("3 - Exit menu")
#     option = int(input("Enter option (1-3): "))
# print("Time for a reset!")


numberList = [] # defines a list
total = 0   # defines a variable
while (len(numberList) < 6):    # while loop that runs while numberList is less than 6
    numberList.append(int(input("Enter a number ")))    # adds a user input to the list
    total += numberList[len(numberList)-1]  # adds the last user input to the total
    print("Your current total is: ", total) # prints the current total
print("Your final total is:", total)    # prints the final total
()
