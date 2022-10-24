import random
def game_start():
    print("Welcome to Hangman")
    global words
    global user_guess
    global rnd_word
    words = 'python', 'java', 'javascript', 'php', 'ruby', 'kotlin'
    rnd_word = random.randint(0, 5)
    print(words[rnd_word])
    user_guess = input("Guess the word: ")

def start_condition():
    game_start()
    if words[rnd_word] == user_guess:
        print("You win!")
    else:
        print("You lose!")
    start_condition()
