# PasswordGenerator
This is a XK Password Generator written in python. It still has a long way to go (adding new password formats and customization options).

# Generating a password
The program runs on a single input command:

```
$ random
```
This will give you a password with the default options {two digit number} - {word1} - {word2} - {word3} 
* **70-vernon-table-dell**
* **89-discounted-tests-really**

## Aditional arguments
You can pass up to 3 aditional arguments:
* Capitalize first letter or each word
* Select separator
* Choose number of words


```
$ random true % 4 
```
* **55%Pentium%Instruments%Roller%Assuming**
```
$ random false _ 2
```
* **30_jimmy_holy**

### Leaving defaults
You can also enter less arguments:
```
$ random & 2
```
* **67&hayes&stats** \
This will pass the arguments of *separator* and *number of words*, leaving capitalize at its default (false)

```
$ random true 4
```
* **80-Pacific-Attempted-Weapon-Bacon** \
This passes the arguments of *capitalize* and *number of words*, leaving separator as default ('-')

#### Note
You must enter the arguments in the correct order, even if you want to leave some at default.

 
