import random
def game_start():
    print("Welcome to Hangman")
    global words
    global user_guess
    global rnd_word
    words = 'python', 'java', 'javascript', 'php', 'ruby', 'kotlin'
    rnd_word = random.randint(0, 5)

game_start()

def user_word():
    global guessed_word_list
    global user_guess
    guessed_word_list = list(words[rnd_word])
    i=-1
    for j in guessed_word_list:
        i += 1
        if(i>=3):
            guessed_word_list[i]="-"

    user_guess = input("Guess the word " + "".join(map(str,guessed_word_list)) + ": ")
user_word()


def win_condition():
    if words[rnd_word] == user_guess:
        print("You win!")
    else:
        print("You lose!")

win_condition()
