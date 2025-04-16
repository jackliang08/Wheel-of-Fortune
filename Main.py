import Wheel
import turtle
import random


t = turtle.Turtle()
w = Wheel.Wheel(t,5)
phrases = ["A BLESSING IN DISGUISE","HISTORY IN THE MAKING","I HAVE AN ANNOUNCEMENT TO MAKE","NOTHING TO LOSE AND EVERYTHING TO GAIN","PASSED WITH FLYING COLORS"]
phrase = random.choice(phrases)
letters = []
turn = 0
p1,p2 = 0,0

w.makeCircle()
w.makeSectors(6)

while True:
    w.pickSector()
    print("P1 Turn!") if turn % 2 == 0 else print("P2 Turn!")
    money = random.randrange(150,950)
    print("Worth $" + str(money))
    guess = str(input("Letter: ")).upper()

    count = 0
    newString = ""
    for l in phrase:  # Checks for all cases for the guess
        if l == guess and l not in letters:
            count += 1
            letters.append(l)
            newString += guess.upper()
        elif l in letters:
            newString += l.upper()
        elif l == " ":
            newString += " "
        else:
            newString += "_"

    print(newString)

    if turn % 2 == 0:  # Determines who gets the money
        p1 += money * count
    else:
        p2 += money * count

    if count == 0:  # If the player didn't guess a letter, the turn advances
        turn += 1

    if newString == phrase:  # At the end, the while loop breaks
        break

print("P1 Earnings: $" + str(p1))
print("P2 Earnings: $" + str(p2))
turtle.done()
