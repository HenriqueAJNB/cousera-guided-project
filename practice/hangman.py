import random


correct_letters = []


def get_random_word_from_file(filename):
    """
    Returns a random word from a list of words saved in a text file.

    Args:
      filename: The name of the text file containing the list of words.

    Returns:
      A random word from the text file.
    """

    with open(filename, "r") as f:
        words = f.read().splitlines()
    random_word_index = random.randint(0, len(words) - 1)
    return words[random_word_index]


# Get a random word from the "words.txt" file.
random_word = get_random_word_from_file("words.txt")

# Print the random word.
print(random_word)

# Write a code that hides the secret word

hidden_word = "_" * len(random_word)
print(hidden_word)

user_input = ""

while len(user_input) > 1 or not user_input.isalpha():
    user_input = input("Enter a single letter: ")

# If the user entered a single letter, store it in a variable
letter_guessed = user_input[0]

# Print the letter
print("You entered the letter:", letter_guessed)

# Check if the user's input character is in the secret word
if letter_guessed in random_word and letter_guessed not in correct_letters:
    # Add the character to the list of correct letters
    correct_letters.append(letter_guessed)

    # Reveal the letter on the game board
    for i in reversed(range(len(hidden_word))):
        if hidden_word[i] == "_":
            hidden_word = hidden_word[:i] + letter_guessed + hidden_word[i + 1 :]

    print(hidden_word)
