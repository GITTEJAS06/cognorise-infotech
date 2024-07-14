import random

# Word list
words = ["python", "programming", "computer", "science", "algorithm", "database", "network", "software", "developer"]

# Hangman figures
hangman_figures = [
    """
       -----
       |   |
           |
           |
           |
           |
    -------""",
    """
       -----
       |   |
       O   |
           |
           |
           |
    -------""",
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    -------""",
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    -------""",
    """
       -----
       |   |
       O   |
      /|\  |
           |
           |
    -------""",
    """
       -----
       |   |
       O   |
      /|\  |
      /    |
           |
    -------""",
    """
       -----
       |   |
       O   |
      /|\  |
      / \  |
           |
    -------"""
]

def select_random_word(words):
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def play_hangman():
    word = select_random_word(words)
    word_letters = set(word)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    guessed_letters = set()
    
    lives = 6
    
    while len(word_letters) > 0 and lives > 0:
        print("\nYou have", lives, "lives left.")
        print("Guessed letters:", ' '.join(guessed_letters))
        
        word_list = [letter if letter in guessed_letters else '_' for letter in word]
        print(hangman_figures[6 - lives])
        print("Current word:", ' '.join(word_list))
        
        guess = input("Guess a letter: ").lower()
        if guess in alphabet - guessed_letters:
            guessed_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
                print("Good guess!")
            else:
                lives = lives - 1
                print("Wrong guess.")
        elif guess in guessed_letters:
            print("You've already guessed that letter. Try again!")
        else:
            print("Invalid character. Please enter a letter.")
    
    if lives == 0:
        print(hangman_figures[6])
        print("Sorry, you died. The word was", word)
    else:
        print("Congratulations! You guessed the word", word, "!!")

def main():
    while True:
        play_hangman()
        if input("Play Again? (Y/N) ").lower() != 'y':
            break
    print("Thanks for playing Hangman!")

if __name__ == "__main__":
    main()
