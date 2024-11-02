import random

# Load word list from file
wordlist = ["apple", "banana", "cherry", "date", "elderberry"]

def choose_word(wordlist):
    return random.choice(wordlist)

def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    guessed_word = ""
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter + " "
        else:
            guessed_word += "_ "
    return guessed_word.strip()

def get_available_letters(letters_guessed):
    available_letters = ""
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if letter not in letters_guessed:
            available_letters += letter
    return available_letters

def match_with_gaps(my_word, other_word):
    my_word = my_word.replace(" ", "")
    if len(my_word) != len(other_word):
        return False
    for i in range(len(my_word)):
        if my_word[i] != "_" and my_word[i] != other_word[i]:
            return False
    return True

def show_possible_matches(my_word):
    my_word = my_word.replace(" ", "")
    matches = [word for word in wordlist if match_with_gaps(my_word, word)]
    if matches:
        print(" ".join(matches))
    else:
        print("No matches found")

def hangman(secret_word):
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("You have", guesses_remaining, "guesses left.")
    print("Available letters:", get_available_letters(letters_guessed))
    while guesses_remaining > 0:
        guess = input("Please guess a letter: ").lower()
        if guess == "*":
            print("Possible word matches are:")
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            continue
        if len(guess) != 1:
            print("Please enter a single letter.")
            warnings_remaining -= 1
            print("You have", warnings_remaining, "warnings left.")
            continue
        if guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter a letter.")
            warnings_remaining -= 1
            print("You have", warnings_remaining, "warnings left.")
            continue
        if guess in letters_guessed:
            print("You've already guessed that letter.")
            warnings_remaining -= 1
            print("You have", warnings_remaining, "warnings left.")
            continue
        letters_guessed.append(guess)
        if guess not in secret_word:
            guesses_remaining -= 1
            print("Oops! That letter is not in my word.")
        else:
            print("Good guess!")
        print(get_guessed_word(secret_word, letters_guessed))
        print("You have", guesses_remaining, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations, you won!")
            print("Your total score for this game is:", guesses_remaining * len(set(secret_word)))
            return
    print("Sorry, you ran out of guesses. The word was", secret_word)

# Play the game
secret_word = choose_word(wordlist)
hangman(secret_word)
