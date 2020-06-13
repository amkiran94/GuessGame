# Guessing Game
# Two Players Game
# First player Enters Some Secret Name and the Second Player Have to guess


Sec_word = input("Enter the secret name?")
guess = ""  # stores the guessed value
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != Sec_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter the guess:")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of Guesses, You  Lost!!")
else:
    print("You Win!")
