import random
import string


word_list = []

with open('Words.txt', 'r') as file:
  for i in file:
    word_list.append(i[:-1])


def generate_password(foo, separator, words):

  random_words = []
  for i in range(words):
    random_words.append(random.choice(word_list))

  if foo:
    for i in random_words:
      random_words[random_words.index(i)] = random_words[random_words.index(i)].title()
  
  password = '{digits}'.format(digits=random.randint(10,100))

  for i in random_words:
    password = password + '{punctuation}{word0}'.format(punctuation=separator, word0=random_words[random_words.index(i)])

  return password


def str2bool(v):
  return v.lower() in ("true", "1")


def run():
  raw = input('Enter your command: ')
  raw_list = raw.split()

  options = ['random', False, '-', 3]

  for i in raw_list:
    options[raw_list.index(i)] = i
  
  if len(raw_list) == 2:
    if raw_list[1] in string.punctuation:
      options[2] = raw_list[1]
    
    elif raw_list[1] in string.digits:
      options[3] = raw_list[1]
  
  elif len(raw_list) == 3:
    if len(raw_list[1]) > 1 and raw_list[2] in string.punctuation:
      print('caso 1')
      options[1] = raw_list[1]
      options[2] = raw_list[2]
    
    elif raw_list[1] in string.punctuation and raw_list[2] in string.digits:
      print('caso 2')
      options[2] = raw_list[1]
      options[3] = raw_list[2]

    elif len(raw_list[1]) > 1 and raw_list[2] in string.digits:
      print('caso 3')
      options[1] = raw_list[1]
      options[3] = raw_list[2]

  


  if options[0] == 'random':
    password = generate_password(str2bool(str(options[1])), options[2], int(options[3]))
    print(password)

run() 