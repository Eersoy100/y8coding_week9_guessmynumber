print("you have 5 guesses!")
import random
from random import randint
correct = random.randint(0, 100)
number = None
lives = 0
while number != correct:    
    number = int(input("what is my number?"))
    if number > correct:
            print("LOWER!")
    five_less = correct - 5
    five_more = correct + 5
    if number < correct: 
            print("HIGHER!")
    if number == correct:
            print("YOU WIN!")
    elif number >= five_less and number <= five_more:
            print("ALMOST! WITHIN 5 AWAY!")
    lives + 1
    if lives > 5:
        print("GAME OVER")
        print("the number was", correct)
        exit 
