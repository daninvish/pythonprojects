import  random

print("Hi friend this is a guessing number game. Stay cool and warm yourself \n"
      "You have to be the best ever. Enjoy it!. You have 5 chances to make it")
number_to_guess = random.randint(1, 10)

chances = 5
guess_counter = 0
while guess_counter < chances:
    guess_counter += 1
    my_guess = int(input("Enter a number:: "))
    if my_guess == number_to_guess:
        print(f"Congratulation you have made it. You guessed the number {number_to_guess} \n"
              f"in {guess_counter} times")
        break
    elif my_guess < number_to_guess:
        print("You guessed to low!")
    elif my_guess > number_to_guess:
        print("you guessed to high")
    else:
        print("try again")
print(f'Oops sorry, The number is {number_to_guess} better luck next time')