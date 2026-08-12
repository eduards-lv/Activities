import random
import string

class Game:
  def __init__(this, max_lives=6):
    this.max_lives=max_lives;

  def play(this):
    secret = this.get_random_word()
    blanks = this.make_blanks(secret)
    lives = this.max_lives
    used = set()

    print("\nWelcome to Word Guessing!")
    print(f"The word has {len(secret)} letters.")
    print(" ".join(blanks))

    while True:
        # Ask the user to guess a letter
        guess = this.prompt_for_letter(used)
        used.add(guess)

        # Is the guessed letter in the word?
        if this.reveal_letters(secret, blanks, guess):
            print("\n Well done, Nice job! You found a letter.")
            print(" ".join(blanks))
            # Are all blanks filled?
            if this.all_blanks_filled(blanks):
                print("\n Congratulation! You guessed the word!")
                print(f"Word: {secret}")
                print("GAME OVER")
                break
        else:
            # Lose a life
            lives -= 1
            print(f"\nNope. You lose a life. Lives left: {lives}")
            print(" ".join(blanks))

            # Have they run out of lives?
            if lives <= 0:
                print("\n Out of lives & Sad story!")
                print(f"The word was: {secret}")
                print("GAME OVER")
                break

        # (loop continues to ask for another letter)

  def make_blanks(this, word):    
    return ["_" for _ in word]

  def all_blanks_filled(this, blanks): 
    return "_" not in blanks      

  def reveal_letters(this, word, blanks, letter):

    found_any = False
    for i, ch in enumerate(word):
        if ch == letter and blanks[i] == "_":
            blanks[i] = letter
            found_any = True
    return found_any
  
  def get_random_word(this):
    
    words = [
        "python", "variable", "function", "iterator", "notebook",
        "pipeline", "dataset", "computer", "research", "analytics"
    ]
    return random.choice(words)

  def prompt_for_letter(this, used_letters):
    while True:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1 or guess not in string.ascii_lowercase:
            print(" → Please enter a single A-Z letter.")
            continue
        if guess in used_letters:
            print(" → You already tried that letter.")
            continue
        return guess


def main():
  game=Game()
  game.play()

if __name__ == "__main__":
    main()