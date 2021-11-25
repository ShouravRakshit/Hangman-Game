import random
import requests


def secret_word():

    API_KEY = "ghy6029na21l9n9hb7pomyjw8n5iwfihjur63n5c6hbt07jzg"
    URL = "https://api.wordnik.com/v4/words.json/randomWords"

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {"hasDictionaryDef": "true",
              "maxCorpusCount=": -1,
              "minDictionaryCount": 1,
              "maxDictionaryCount=": -1,
              "minLength": 5,
              "maxLength": -1,
              "limit": 100,
              "api_key": API_KEY
              }

    # sending get request and saving the response as response object
    response = requests.get(url=URL, params=PARAMS)

    # extracting data in json format
    random_words = []
    data = response.json()
    for word in data:
        random_words.append(word["word"])
    return random_words


# giving a difficulty.
def game_difficulty(rand_words):
    difficult = input("Easy or Medium or Hard")

    if difficult.lower() == "easy":
        new_list = [word for word in rand_words if len(word) <= 6]
        random_word = random.choice(new_list)
        return random_word

    elif difficult.lower() == "medium":
        new_list = [word for word in rand_words if 7 <= len(word) <= 10]
        random_word = random.choice(new_list)
        return random_word

    elif difficult.lower() == "hard":
        new_list = [word for word in rand_words if 11 <= len(word) <= 13]
        random_word = random.choice(new_list)
        return random_word


rand_words = secret_word()
guess_word = (game_difficulty(rand_words))
# The secret word
print(guess_word)
bad_guess = ""
lives = 5
dash = ""
print("The secret word looks like: ", end="")

# creating the blank boxes.
for _ in range(len(guess_word)):
    dash = dash + "_"
print(dash)

while lives > 0:
    print(f"You have {lives} guesses remaining")
    print("What's your next guess?", end="")
    user_input = input()
    if user_input in dash:
        print("You have already guessed this letter! \n")
    else:
        # checking if the user input letter matches any letter with the secret word.
        if user_input in guess_word:
            for char in range(len(guess_word)):
                if user_input == guess_word[char]:
                    list1 = list(dash)
                    list1[char] = user_input
                    dash = ''.join(list1)
            print("Nice guess! \n")
    #  checking if the user input letter does not matches with any letter with the secret word.
    if user_input not in guess_word:
        print(f'Sorry, there is no "{user_input}". \n')
        lives = lives - 1
        if lives == 0:
            print("GAME OVER!")
            break

    print("The secret word looks like: ", end="")
    print(dash)
    # checking if the user input letter does not matches with any letter with the secret word and lives is less than 5.
    if lives < 5 and user_input not in guess_word:
        bad_guess = bad_guess + user_input
        print(f"Your bad guesses so far: {bad_guess}")
    # checking if there is any empty box.
    if "_" not in dash:
        print("Nice guess! Congratulations!")
        break

