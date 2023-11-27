# Python space quiz first project for Devrim!

print("Welcome to my quiz!")

name = input("what is your name? ").title()

print(f"Hello {name}")

playing = input("would you like to start the quiz? ").lower()

if playing != "yes":
    quit()
print("OK! let's get started! :) ")
score = 0

question = input("what planet do we live on? ").lower()
if question == "earth":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

question = input("What is the name of the biggest planet? ").lower()
if question == "jupiter":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

question = input("What is the closest planet to the Sun? ").lower()
if question == "mercury":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

question = input("Earth is located in which galaxy? ").lower()
if question == "milkyway":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


question = input("Who was the first person to walk on the moon? ").lower()
if question == "neil armstrong":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

question = input("is the sun a star or a planet? ").lower()
if question == "star":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f"Great work {name}, You Answered {score} questions correct!")
