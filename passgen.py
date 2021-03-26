import random
import string

def generate_word_list():
  word_list = []

  with open('Words.txt', 'r') as file:
    for i in file:
      word_list.append(i[:-1])
  
  return word_list


def generate_xk(foo, separator, words):
  
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
  
  return password

def generate_morph(word):
  # split_word = [char.lower() for char in word]
  split_word = list(word) 
  
  transformations = {                 # Dictionary to list character transformations
                      'l':'1', 
                      'i':'!', 
                      'o':'0', 
                      'A':'4'
  } 
  
  for w in split_word:
    
    if w in transformations:
      split_word[split_word.index(w)] = transformations[w]

  return ''.join(split_word)

if __name__ == '__main__':
  print(generate_morph(input()))