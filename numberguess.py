import random

top_of_range = input("Type a Number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0 :
        print("enter a number greater then 0")
        quit()
else:
    print("enter a number")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('enter a number')
        continue

    if user_guess == random_number:
        print("got it ")
        break
    else:
        print("you got wrong")
        quit()

print(guesses)

