# python 3
# highter_lower game : entertainment
from game_data import data
import art
import random
from replit import clear
import time

person_a = random.choice(data)
score = 0

while True:  
  person_b = random.choice(data)
  # to avoid choosing the same person
  while person_a == person_b :
    person_b = random.choice(data)
  print(art.logo)  
  print(f"A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}  ")
  print(art.vs)
  print(f"B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}")
  answer = input('Who has more follower in millions? A or B: ').upper()

  a_num = person_a['follower_count']
  b_num = person_b['follower_count']
  if a_num > b_num:
    correct_answer = "A"
  elif a_num < b_num:
    correct_answer = "B"
    person_a = person_b
  if correct_answer != answer:
    print('\nYou are wrong. GAME OVER')
    print(f"Your total score is {score}")
    break
  else:
    print("\nRight")
    score += 1
    print(f"score : {score}")
    time.sleep(1)
    clear()
    
