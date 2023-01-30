# python
# Blackjack.py 
import random
from replit import clear
import black_art

cards = [11,2,3,4,5,6,7,8,10,10,10]
new = True

def blackjack(card_list):
  if 10 in card_list and 11 in card_list:
    blackjack=True
    return blackjack
  

def next_card():
  user_card.append(random.choice(cards))
  user_sum = sum(user_card)
  if 11 in user_card and user_sum >= 20:
    user_card.remove(11)
    user_card.append(1)
  print(f'\nUser cards : {user_card}')
  print(f'User score : {user_sum}')
  if user_sum > 21:
    print('BONK! : you fail')
    game = False
    return game
  
      
  
while new:
  user_card = []
  computer_card = []
  user_sum = 0
  computer_sum = 0
  print(black_art.logo)
  for i in range(2):
    user_card.append(random.choice(cards))
    computer_card.append(random.choice(cards))
  print(f'User cards : {user_card}')
  print(f"Computer's first card :  {computer_card[0]}")
  
  while True:
    if blackjack(user_card) == True:
      print(f"User cards : {user_card}")
      print('User has blackjack')
      print('User wins')
      break
    if blackjack(computer_card) == True:
      print(f"Computer cards : {computer_card}")
      print('Computer has blackjack')
      print('Computer wins')
      break
      
    more_card = input('Do you want to draw another card? Yes or No : ').lower()
    if more_card == 'yes':
      next_draw = next_card()
      if next_draw == False: # user failed by drawing over 21
        break
    elif more_card == 'no':
      user_sum= sum(user_card)
      print(f"User cards : {user_card}")
      print(f"User score : {user_sum}")
      while computer_sum < 16:
        computer_card.append(random.choice(cards))
        computer_sum= sum(computer_card)
        if 11 in computer_card and computer_sum >= 20:
          computer_card.append(1)
          computer_card.remove(11)
          computer_sum = sum(computer_card)
      print(f'Computer cards : {computer_card}')
      print(f"Computer scores : {computer_sum}")
      print(f'\nComputer score: {computer_sum}')
      print(f"User score: {user_sum}")
      if computer_sum > 21:
        print('You wins.')
        break
      elif computer_sum > user_sum:
        print('Computer wins')
      elif user_sum > computer_sum:
        print('You win')
  new_game= input('Do you want to start a new game? Yes or No ').lower()
  if new_game == "no":
    new = False
    clear()
    print(black_art.logo)
    print('Goodbye')
  else:
    clear()
      
  
      
      
      
    
      

