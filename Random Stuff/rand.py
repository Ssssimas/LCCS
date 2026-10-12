import random

def Roll(numbers, outOf):
    Correct = 0
    RollList = []
    for i in range(numbers):
        RollList.append(random.randint(1,outOf))
        if (RollList[i] == 1):
            Correct += 1
    if (Correct == numbers):
        print("WIN")
    
    print(RollList)
    
Roll(3, 3)