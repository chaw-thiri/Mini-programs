import random
from replit import clear
from guess_art import logo
level = {"easy":10, "normal":7, "hard":5,}
new_game = True


while new_game:
  number = random.randint(1,100)
  print(logo)
  user_level= input('Choose your level: easy, normal or hard : ').lower()
  chance= level[user_level]
  
  while chance != 0:
    print(f"\nYou have {chance} chances.")
    guess = int(input("Guess your number : "))
    if guess == number : 
      print('Congratulations')
      break
    elif guess <= number:
      print('Too low')
    elif guess >= number :
      print('Too high')
    chance -= 1  
  if chance == 0:
    print('You have used all of your chances.')
    print(f"The correct number is {number}")
  new = input('Do you want to start a new game? y or n :').lower()
  clear()
  
  if new == 'n':
    print(logo)
    print('Goodbye')
    break
    



