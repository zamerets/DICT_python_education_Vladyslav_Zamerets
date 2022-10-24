import random
right = 0
att = 8
repeat = True
def game_start():
    print("Welcome to Hangman")
    global words
    global user_guess
    global rnd_word
    words = 'python', 'java', 'javascript', 'php', 'ruby', 'kotlin'
    rnd_word = random.randint(0, 5)
game_start()
main_word = list(words[rnd_word])

print(main_word)

def user_word():
    global guessed_word_list
    global user_guess
    guessed_word_list = list(words[rnd_word])
    i=-1
    for j in guessed_word_list:
        i += 1
        guessed_word_list[i]="-"
    print("".join(map(str,guessed_word_list)))
user_word()
def main_function():
    user_guess = input("Guess a letter: ")
    for k in guessed_word_list:
        if (k == user_guess):
            print("No improvments!")
            main_function()
            return
    def comparing():
        i=-1
        global ugadal
        ugadal = False
        for k in main_word:
            i+=1
            if user_guess == k:
                guessed_word_list[i] = k
                ugadal = True

    comparing()
    print(str(ugadal))
    def word_output():
        global att
        print(guessed_word_list)
        if ugadal == False:
            att -= 1
            print("That letter doesn't appear in the word")
            print(str(att))
    word_output()

while att > 0:
    main_function()







#Условия выигрыша
def win_condition():

    if words[rnd_word] == user_guess:
        print("You win!")
    else:
        print("You lose!")

