print("welcome to my quiz")

playing = input("Do yo want to play? ")
if playing.lower() != "yes":
    quit()

print("okay! let's play :")
score = 0

answer = input("what does cpu stand for? ")
answer = answer.lower()
if answer == "central processing unit" :
    print("correct")
    score += 1
else:
    print("incorrect")

answer = input("what does gpu stand for? ")
answer = answer.lower()
if answer == "graphics processing unit" :
    print("correct")
    score += 1
else:
    print("incorrect")

answer = input("what does RAM stand for? ")
answer = answer.lower()
if answer == "random acess memory" :
    print("correct")
    score += 1
else:
    print("incorrect")

answer = input("what does psu stand for? ")
answer = answer.lower()
if answer == "power supply" :
    print("correct")
    score += 1
else:
    print("incorrect")


print("your got " + str(score) + " questions correct")
print("your got " + str((score / 4) * 100) + " %. ")