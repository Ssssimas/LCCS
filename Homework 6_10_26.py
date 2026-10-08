
counterFor = 11
for x in range(counterFor):
    print (x)

counterWhile = 1
while counterWhile <= 10:
    print (counterWhile)
    counterWhile +=1



###################################################

userInput = int(input("Input a number "))

for x in range(userInput):
    if x % 2 == 1:
        print(x)
