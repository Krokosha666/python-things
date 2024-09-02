import math

# this script is used to find best price for something with when commision is applied and result is rounded, the benefactor gets less money 
# idk its this brain impulse i had and couldnt find what im describing in normal calculators

percentage = int(input("Percentage %: ") or 70) / 100
increments = int(input("Increments: ") or 1)
startfrom = int(input("Start from: ") or 0)
endat = int(input("End at: ") or 0)
if endat ==0:
    print("Press enter to iterate...")

print()

counter = startfrom
foundSomething = False
while True:


    if endat == 0:
        if foundSomething:
            input()
    elif counter > endat:
        quit()
        break
    foundSomething = False


    counter += increments

    result = counter * percentage
    res1,res2 = math.modf(result)
    if res1 > 0.5 and res1 < 0.7:
        print(counter," = ", result)
        foundSomething = True



quit()