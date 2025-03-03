import random 


chance = 7
computer_number = random.randrange(10,100)
print(computer_number)
counter  = 0
user_number = 0

while counter < chance:
    counter += 1
    user_number = int(input("enter the guess number!🤔"))

    if user_number == computer_number:
        print(f"You have guessed the correct number!😎 the number was {computer_number}")
        break
    elif counter >= chance and user_number != computer_number:
        print(f"Sorry! out of attempts! the number was {computer_number}😁")
    elif user_number > computer_number:
        print("ooops the number is high! try again")
    elif user_number < computer_number:
        print("ooops the number is low! try again")

