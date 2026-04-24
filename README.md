import random
def hangman_game():
   
    words = ["python", "hangman", "computer", "programming", "keyboard"]
    
    
    secret_word = random.choice(words).lower()
    word_letters = set(secret_word) 
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6
    
    print("Welcome to Hangman!")
    print("Guess the word one letter at a time. You have 6 incorrect guesses allowed.")
    print(f"Word length: {len(secret_word)} letters\n")
    
   
    while incorrect_guesses < max_incorrect and len(word_letters) > 0:
      
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(display_word)
        print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")
        print(f"Guessed letters: {' '.join(sorted(guessed_letters))}\n")
        
    
        guess = input("Enter a letter: ").lower().strip()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter!\n")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter!\n")
            continue
        
        
        guessed_letters.add(guess)
        
        if guess in word_letters:
            word_letters.discard(guess)
            print("Good guess!\n")
        else:
            incorrect_guesses += 1
            print("Wrong guess!\n")
    
    print("\n" + "="*30)
    if incorrect_guesses < max_incorrect:
        print("Congratulations! You won!")
    else:
        print("Game Over! You lost.")
    print(f"The word was: {secret_word}")
    print("="*30)

if __name__ == "__main__":
    hangman_game()
