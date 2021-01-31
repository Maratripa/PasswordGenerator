import random


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

  if options[0] == 'random':
    password = generate_password(str2bool(options[1]), options[2], int(options[3]))
    print(password)

run()