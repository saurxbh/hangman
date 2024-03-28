import sys, random

# Set up the constants
HANGMAN_PICS = [r"""
 +--+
 |  |
    |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
 |  |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|  |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
/   |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
/ \ |
    |
====="""]

CATEGORY = 'Animals'
WORDS = 'ANT BABOON BADGER BAT BEAR BEAVER CAMEL CAT CLAM COBRA COUGAR COYOTE CROW DEER DOG DONKEY DUCK EAGLE FERRET FOX FROG GOAT GOOSE HAWK LION LIZARD LLAMA MOLE MONKEY MOOSE MOUSE MULE NEWT OTTER OWL PANDA PARROT PIGEON PYTHON RABBIT RAM RAT RAVEN RHINO SALMON SEAL SHARK SHEEP SKUNK SLOTH SNAKE SPIDER STORK SWAN TIGER TOAD TROUT TURKEY TURTLE WEASEL WHALE WOLF WOMBAT ZEBRA'.split()

def drawHangman(missedLetters, correctLetters, secretWord):
    '''Draw the current state of Hangman, along with the correctly guessed and missed letters of the secret word'''
    print(HANGMAN_PICS[len(missedLetters)])
    print('The category is: ', CATEGORY)
    print()

    # Show the incorrectly guessed letters:
    print('Missed letters: ', end='')
    for letter in missedLetters:
        print(letter, end= ' ')
    if len(missedLetters) == 0:
        print('No missed letters yet.')
    print()

    # Display the blanks for the secret word (one blank per letter)
    blanks = ['_'] * len(secretWord)

    # Replaced blanks with correctly guessed letters
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks[i] = secretWord[i]

    # Show the secret word with spaces in between each letter
    print(' '.join(blanks))


def getPlayerGuess(alreadyGuessed):
    '''Returns the letter the player guessed. This function makes sure the player enters
    a single letter they haven't guessed before.'''
    while True: # Keep asking until the player enters a valid letter
        print('Guess a letter.')
        guess = input('> ').upper()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif not guess.isalpha():
            print('Please enter a LETTER.')
        else:
            return guess


def main():
    # Set up variables for a new game
    missedLetters = [] # List of incorrect letter guesses
    correctLetters = [] # List of correct letter guesses
    secretWord = random.choice(WORDS) # The word the player must guess

    while True: # Main game loop
        drawHangman(missedLetters, correctLetters, secretWord)

        # Let the player enter their letter guess
        guess = getPlayerGuess(missedLetters + correctLetters)

        if guess in secretWord:
            # Add the correct guess to correctLetters
            correctLetters.append(guess)

            # Check if the player has won
            foundAllLetters = True # Start off assuming they've won
            for secretWordLetter in secretWord:
                if secretWordLetter not in correctLetters:
                    # There's a letter in the secret word that isn't
                    # in correctLetters yet, so the player hasn't won
                    foundAllLetters = False 
                    break
            if foundAllLetters:
                print('Yes! The secret word is:', secretWord)
                print('You have won!')
                break # Break out of the main game loop
        else:
            # The player has guessed incorrectly
            missedLetters.append(guess)

            # Check if the player has guessed too many times and lost
            # The -1 is because we don't count the empty gallows in HANGMAN_PICS
            if len(missedLetters) == len(HANGMAN_PICS) - 1:
                drawHangman(missedLetters, correctLetters, secretWord)
                print('You have run out of guesses!')
                print('The secret word was {}'.format(secretWord))
                break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program