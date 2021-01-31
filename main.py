import random
import time
import pyperclip


word_list = []

with open('Words.txt', 'r') as file:
  for i in file:
    word_list.append(i[:-1])


def generate_password(may):

  random_words = [random.choice(word_list), random.choice(word_list), random.choice(word_list)]

  if may:
    for i in random_words:
      random_words[random_words.index(i)] = random_words[random_words.index(i)].title()
  
  password = '{digits}{punctuation}{word1}{punctuation}{word2}{punctuation}{word3}'.format(digits=random.randint(1,100), punctuation='-', word1=random_words[0], word2=random_words[1], word3=random_words[2])

  return password


def manage_input(string):
  pass

def run():
  command, may = input('Enter your command: ').split()

  foo = bool(int(may))
  print(foo)

  if command == 'random':
    password = generate_password(foo)
    print(password)
    
  
run()