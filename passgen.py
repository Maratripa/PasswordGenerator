import random
import string

def generate_word_list():
  word_list = []

  with open('Words.txt', 'r') as file:
    for i in file:
      word_list.append(i[:-1])
  
  return word_list


def generate_password(foo, separator, words):
  
  word_list = generate_word_list()

  random_words = []
  for i in range(words):
    random_words.append(random.choice(word_list))

  if foo:
    for i in random_words:
      random_words[random_words.index(i)] = random_words[random_words.index(i)].title()
  
  password = '{digits}'.format(digits=random.randint(10,99))

  for i in random_words:
    password = password + '{punctuation}{word0}'.format(punctuation=separator, word0=random_words[random_words.index(i)])
  
  print(password)


def str2bool(v):
  return v.lower() in ("true", "1")

'''
def run():
  raw = input('Enter your command: ')
  raw_list = raw.split()

  options = ['random', False, '-', 3]

  
  if len(raw_list) == 2:
    if raw_list[1] in string.punctuation:
      options[2] = raw_list[1]
    
    elif raw_list[1] in string.digits:
      options[3] = raw_list[1]
  
  elif len(raw_list) == 3:
    if len(raw_list[1]) > 1 and raw_list[2] in string.punctuation:
      options[1] = raw_list[1]
      options[2] = raw_list[2]
    
    elif raw_list[1] in string.punctuation and raw_list[2] in string.digits:
      options[2] = raw_list[1]
      options[3] = raw_list[2]

    elif len(raw_list[1]) > 1 and raw_list[2] in string.digits:
      options[1] = raw_list[1]
      options[3] = raw_list[2]

  elif len(raw_list) == 4:
    for i in raw_list:
      options[raw_list.index(i)] = i


  if raw_list[0] == 'random':
    password = generate_password(str2bool(str(options[1])), options[2], int(options[3]))
    print(password)

run() 
'''