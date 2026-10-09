### Task 2: Leaving Cert Grade Bands ###


def grade(grade):
    if grade >= 90:
        print("H1")
    elif grade >=80:
        print("H2")
    elif grade >=70:
        print("H3")
    elif grade >=60:
        print("H4")
    elif grade >=50:
        print("H5")
    elif grade >=40:
        print("H6")
    elif grade >=30:
        print("H7")
    elif grade >=0:
        print("H8")
        
grade(82)
    
### Task 3: Cinema Ticket Pricing ###
    
age = 16
ticketPrice = 0

if age < 5:
    ticketPrice = 0
elif age <= 16:
    ticketPrice = 8
elif age <= 64:
    ticketPrice = 12
elif age > 64:
    ticketPrice = 6

print("Ticket price for age " + str(age) + " is " + str(ticketPrice) + " euro")


### Task 4 (Extension): Catching Invalid Marks ###
        

mark = -5

if mark > 100 or mark < 0:
    print("Invalid Mark")
else:
    grade(mark)