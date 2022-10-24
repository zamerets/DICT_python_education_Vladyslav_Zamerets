print("Welcome to Hangman")

def game_start():
    global words
    global user_guess
    words = "java"
    user_guess = input("Guess the word: ")

def start_condition():
    game_start()
    if words == user_guess:
        print("You win!")
    else:
        print("You lose!")
start_condition()