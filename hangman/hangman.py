# python 
# hangman game
import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
display_list=[]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = 6
status = True

def win():
  if '_' not in display_list:
    print("Congratulations")
    global status 
    status = False

def lose():
  if lives == 0:
    print(stages[lives])
    print('You lose')
    print(f'The correct answer is {chosen_word}')
    global status 
    status = False

def check():
  for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
      display_list[i] = guess
      
  if guess not in chosen_word:
    global lives 
    print(stages[lives])
    lives -= 1
  print(''.join(display_list))
  win()
  lose()
  
# displaying _ for number of alphabets
for i in range(len(chosen_word)):
  display_list.append('_')
print(''.join(display_list))

# asking alphabet from the user 
while status:
  guess = input("\nGuess the letter: ").lower()
  check()
  print('..................................................')
  
    


