# Monday 08 Sept / Tuesday 07 September - Intro to Python

##### REALLY IMPORTANT YOU READ ALL THIS!!! #####
# Use the notes that have been given out to you to answer the following questions over the next 2 days.
# If you are struggling - please make sure you go and ask a few people for help!  Of course you are going
# to struggle, this is brand new for a lot of you, so please be helpful and look after each other!

# The numbers to the left let you know what line you are on.  This is line 8.
# Some questions will ask you to delete the hashtag on a certain line.
# Make sure you do this so that the code runs properly.

# Where I have typed "Answer:" or "Your code:" ---- this is where I want you to put your answer/code
# Just click underneath it to start typing your answer/code

# Reminder: the green "play" button up on the top is how you "run" a program
# MAKE SURE YOU SAVE YOUR FILE EVERY 10 MINS!!!!!!!!

# 10 mins before class finishes, save your file to your desktop
# Open Google Drive
# Create a Folder called Computer Science
# Go into that folder
# Add this file that you have been working on (THAT YOU HAVE SAVED!!) into that folder
# Open up the Assingment I posted on Google Classroom
# Upload this file from your Google Drive to Google Classroom on BOTH MONDAY AND TUESDAY

###########################################################
# Q1

# I have typed out the print statement for you below -  press F5. What happens?

print("My first program")

# Answer: My first program



###########################################################

# Q2

# Now deliberately remove the closing bracket and press F5. What error appears?
# Answer: Syntax error, ( was never closed


###########################################################
# Q3

# Delete the hash tags (#) on line 49 and 50.  Run the following code - what type of error is it?
#x = 10
#print(y)

# Answer: name error, y is not defined


###########################################################
# Q4

# Delete the hashtags on line 60.  This code runs without an error but gives the wrong answer.
# What type of error is it, and what is wrong?
print("The sum of 3 and 4 is", 3 * 4)

# Answer: it says The sum of 3 and 4 is 12, it doesnt give an error


###########################################################
# Q5

# Delete the hashtags on lines 69 - 72.  Predict what the output will be:
print("Monday")
print("Tuesday")
print()
print("Thursday")

# Prediction: prints monday tuesday, a blank row then thursday
# Actual Answer: prints monday tuesday, blank row then Thursday

###########################################################
# Q6

# Write a print() statement that outputs the below exactly - all on one line - using escape characters:
# Name:   Alice
# Age:    17

# Your code:
print("Name: Alice\nAge: 17")


###########################################################
# Q7

# Write a short program that prints your name, school,
# and year - each on a separate line - using only ONE print() statement and escape characters.

# Your code:
print(
    "Simas\n"
    "Beneavin\n"
    "2026")


###########################################################
# Q8
# Delete only the first hastags on lines 101 - 103
# This code has a comment problem. Identify what is wrong with each comment and rewrite it correctly:

#x = x + 1   # adds 1 to x
#total = 0   # total is zero
#results.sort()   # sorts

# What is wrong:	total is zero doesnt tell us the action being done
#                    sorts doesnt tell us how its being sorted
# what it should be:	sets the total to zero
#						sorts in order of lowest to highest

###########################################################
# Q9

# Using only print() with end= and sep= arguments (no escape characters), produce this output:
# 1 | 2 | 3
# 4 | 5 | 6
# Hint: you will need two print() statements.

# Your code:
print("1", "2", "3", sep=" | ")
print("4", "5", "6", sep=" | ")


