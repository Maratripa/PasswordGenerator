import random


word_list = []

with open('Words.txt', 'r') as file:
  for i in file:
    word_list.append(i[:-1])


def generate_password(foo):

  random_words = [random.choice(word_list), random.choice(word_list), random.choice(word_list)]

  if foo:
    for i in random_words:
      random_words[random_words.index(i)] = random_words[random_words.index(i)].title()
  
  password = '{digits}{punctuation}{word1}{punctuation}{word2}{punctuation}{word3}'.format(digits=random.randint(10,100), punctuation='-', word1=random_words[0], word2=random_words[1], word3=random_words[2])

  return password


def run():
  raw = input('Enter your command: ')
  raw_list = raw.split()

  options = ['random', 0]

  for i in raw_list:
    options[raw_list.index(i)] = i

  if options[0] == 'random':
    password = generate_password(options[1])
    print(password)

run()