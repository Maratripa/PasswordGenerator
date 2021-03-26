# PasswordGenerator
This is a XK Password Generator written in python. It still has a long way to go (adding new password formats and customization options).

# Generating a password
The program is bassed on argparse to run and generate a password.
At the time there are two types of password generation available:

### XK Passwords
```
$ python3 main.py xk
```

### Word morphing passwords
```
$ python3 main.py morph
```

## Positional arguments
* xk
* morph

## Optional arguments
You can pass up to 3 aditional arguments:
* --caps    #Capitalize first letter of each word
* --sep     #Choose the separator
* --words   #Choose the number of words to be generated

Each one of the optional arguments has their own default value:
* --caps = false
* --sep = '-'
* --words = 3

### Morph password
After entering the 'morph' positional argument you'llhave to enter a word for the program to morph

### Note
You can run the flag -h to display all posible arguments
```
$ python3 main.py -h
```
