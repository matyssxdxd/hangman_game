from random import choice
from string import ascii_lowercase


def input_check(letter):
    if len(letter) == 0:
        print("Please, input a single letter.")
        return True
    elif len(letter) > 1:
        print("Please, input a single letter.")
        return True
    elif letter not in ascii_lowercase:
        print("Please, enter a lowercase letter from the English alphabet.")
        return True
    if letter in already_guessed:
        print("You've already guessed this letter.")
        return True


win_count = 0
lose_count = 0

while True:
    attempt = 8
    print(f"H A N G M A N # {attempt} attempts")
    action = input("Type \"play\" to play the game, \"results\" to show the scoreboard, and \"exit\" to quit: ")
    if action == "play":
        word = choice(["python", "java", "swift", "javascript"])
        hidden_word = "-" * len(word)
        set_word = set(word)
        already_guessed = []
        while True:
            print(hidden_word)
            guess = input("Input a letter: ")
            if input_check(guess) is True:
                continue
            already_guessed.append(guess)

            if guess in set_word:
                indexes = [i for i, char in enumerate(word) if char == guess]
                for i in range(len(indexes)):
                    new_list = list(hidden_word)
                    new_list[indexes[i]] = word[indexes[i]]
                    hidden_word = "".join(new_list)
            else:
                if attempt == 1:
                    print(f"That letter doesn't appear in the word. # {attempt} attempt")
                else:
                    print(f"That letter doesn't appear in the word. # {attempt} attempts")
                attempt = attempt - 1
            if hidden_word == word:
                print(f"You guessed the word {word}!")
                print(f"You survived!")
                win_count += 1
                break
            elif attempt == 0:
                print("You lost!")
                lose_count += 1
                break
    elif action == "results":
        print(f"You won: {win_count} times")
        print(f"You lost: {lose_count} times")
    elif action == "exit":
        print("Thank you for playing!")
        break
    else:
        print("Incorrect input")
