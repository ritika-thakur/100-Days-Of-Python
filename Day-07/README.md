## Project - 07

# Hangman

``` 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    
```

###  Step - 1

TOdO-1 - Randomly choose a word from the word_list and assign it to a variable called `chosen_word`.

TODO-2 - Ask the user to guess a letter and assign their answer to a variable called `guess` . Make guess lowercase.

TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

### Step - 2

 TODO-1: - Create an empty List called `display`.
#For each `letter` in the `chosen_word`, add a '_' to `display`.
#So if the chosen_word was "apple", display should be `["_", "_", "_", "_", "_"]` with 5 "_" representing each letter to guess.

TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches `guess` then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be `["_", "p", "p", "_", "_"]`.

TODO-3: - Print `display` and you should see the guessed letter in the correct position and every other letter replace with ` _ `.

### Step - 3

TODO-1: Use a while loop to let the user guess again. The loop should stop only once the user has guessed all the words in the `chosen_word` and `display` has no more "_". Then you can tell the user they have won.

### Step - 4

TODO-1: - Create a variable called `lives` to keep track of the number of lives left. 
#Set `lives` to equal 6.

#TODO-2: - If guess is not a letter in the chosen_word,
#Then reduce `lives` by 1. 
#If lives goes down to 0 then the game should stop and it should print `You lose`.

#TODO-3: - print the ASCII art from `stages` that corresponds to the current number of `lives` the user has remaining.

### Step - 5

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

#TODO-2: - Import the logo from hangman_art.py and print it at the start of the game.

#TODO-3: - If the user has entered a letter they've already guessed, print the letter and let them know.

#TODO-4: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.

## Output

```


 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    



['_', '_', '_', '_', '_']
Guess a letter: p
Lives Left:  5
['_', '_', '_', '_', '_']

  +---+
  |   |
  O   |
      |
      |
      |
=========

Guess a letter: a
Lives Left:  4
['_', '_', '_', '_', '_']

  +---+
  |   |
  O   |
  |   |
      |
      |
=========

Guess a letter: t
Lives Left:  3
['_', '_', '_', '_', '_']

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
Guess a letter: e
Lives Left:  3
['_', '_', '_', 'e', '_']

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
Guess a letter: p
Lives Left:  2
['_', '_', '_', 'e', '_']

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========

Guess a letter: d
Lives Left:  1
['_', '_', '_', 'e', '_']

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========

Guess a letter: l
You lose. The correct word is:  vixen
Lives Left:  0
['_', '_', '_', 'e', '_']

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
```
