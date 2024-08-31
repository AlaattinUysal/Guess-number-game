import random
from art import logo
from replit import clear


number_choice = random.randint(1,100)
print("I'm thinking of a number between 1 and 100.")
#print(f"psst the answer is {number_choice}")


def play_game():
  print(logo)
  print("Welcome to the Number Guessing Game! ")
  def number_guess():
    if my_choice > number_choice:
      return "too high"
    elif my_choice < number_choice:
      return "too low"
    elif my_choice == number_choice:
      return f"You got it! The answer was {number_choice}!"
  if input("Choose a difficulty : Type 'easy' or 'hard': ") == 'easy':
    my_choice_number = 10
    print(f"You have {my_choice_number} attempts remaining to guess the number.")
    while my_choice_number > 0:
      my_choice = int(input("Make a guess: "))
      my_choice_number -= 1
      print(number_guess())
      if my_choice == number_choice:
        my_choice_number = 0
      else:
        if my_choice_number == 0:
           print("You've run out of guesses , you lose")
        else:
          print("Guess again.")
          print(f"You have {my_choice_number} attempts remaining to guess the number.")

  else:
    my_choice_number = 5
    print(f"You have {my_choice_number} attempts remaining to guess the number.")
    while my_choice_number > 0:
      my_choice = int(input("Make a guess: "))
      my_choice_number -= 1
      print(number_guess())
      if my_choice == number_choice:
        my_choice_number = 0
      else:
       if my_choice_number == 0:
         print("You've run out of guesses , you lose")
       else:
        print("Guess again.")
        print(f"You have {my_choice_number} attempts remaining to guess the number.")


    
while input("Do you want to play a game of Guessing The Number? Type 'y' or 'n' ? : ") == 'y' :
 clear()
 play_game()
