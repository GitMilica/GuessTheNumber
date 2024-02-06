from random import randint

print("Welcome to the Number Guessing Game!")
print("I'am thinking of a number between 1 and 100.")
random_num = randint(1, 100)

level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

print(f"The secret number is {random_num}")
end_game = True


def easy_game():
  attempts = 10
  while attempts != 0:
    guess = int(input("Make a guess: "))
    attempts -= 1
    
    if attempts == 0:
      print("You've run out of guesses, you lose.")
    elif guess > random_num:
      print("Too high.\nGuess again.")
      print(f"You have {attempts} attempts remaining to guess the number.")
    elif guess < random_num:
      print("Too low.\nGuess again.")
      print(f"You have {attempts} attempts remaining to guess the number.")
    elif guess == random_num:
      print(f"You got it! The answer was {random_num}.")
      return end_game == False
         

def hard_game():
  attempts = 5
  while attempts != 0:
    guess = int(input("Make a guess: "))
    attempts -= 1
    if attempts == 0:
      print("You've run out of guesses, you lose.")
    elif guess > random_num:
      print("Too high.\nGuess again.")
      print(f"You have {attempts} attempts remaining to guess the number.")
    elif guess < random_num:
      print("Too low.\nGuess again.")
      print(f"You have {attempts} attempts remaining to guess the number.")
    elif guess == random_num:
      print(f"You got it! The answer was {random_num}.")
      return end_game == False
      


if level == "easy":
  print("You have 10 attempts remaining to guess the number.")
  easy_game()
elif level == "hard":
  print("You have 5 attempts remaining to guess the number.")
  hard_game()
  
 