import random
import math
#Taking inputs
lower = int(input("Enter Lower bound:-    "))
#Taking inputs
upper = int(input("Enter Upper bound:-    "))

#Generating random number between
#lower and upper
x= random.randint(lower, upper)
print("\n\tyou've only",
      round(math.log(upper-lower+1, 2)),
      "chances to guess the integer!\n")

#initializing the number of zeros
count = 0
#for calculating the minimum number of
#guesses depends upon range
while count< math.log(upper-lower+1,2):
    count+=1
    #taking number as input
    guess = int(input("guess a number:-"))
    #condition testing
    if x == guess:
        print("Congradulations you did it in",
              count, "try")
    #once guess loop will break
        break
    elif x > guess:
         print("you guessed too small")
    elif x<guess:
        print("you guessed too high")

#if guessing is more than required guesses,
#shows this output
if count>= math.log(upper-lower+1,2):
    print("\nthe number is %d" %x)
    print("\tbetter luck next time!")





