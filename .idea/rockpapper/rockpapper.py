import random
import re
user_actions = ["rock", "paper", "scissors", "!exit", "!rating"]
exit_game = False
class Game:
    def __init__(self, user_figure, winner,bot_figures_list, bot_figure):
        self.user_figure = user_figure
        self.winner = winner
        self.bot_figures_list = bot_figures_list
        self.bot_figure = random.choice(self.bot_figures_list)
    def winner_figure(self):
        if self.bot_figure == self.user_figure:
            self.winner = None
        else:
            match self.user_figure:
                case "rock":
                    if self.bot_figure == "paper":
                        self.winner = "bot"
                case "paper":
                    if self.bot_figure == "scissors":
                        self.winner = "bot"
                case "scissors":
                    if self.bot_figure == "rock":
                        self.winner = "bot"
            if self.winner != "bot":
                self.winner = "user"
            return self.winner

def rating():
    with open("res.txt", 'r') as file:
        rating_arr = file.readlines()
        for line in rating_arr:
            if name in line:
                if line[-1] == ' ' or line[-1] == ':':
                    print(f"Your score is: {score}")
                else:
                    print(f"Your score is: {score}")


score = 0
name = input("Enter your name: ")
print(f"Hi {name}")
user_doesnotexist = True
with open("res.txt", 'r') as file:
    file_lines = file.readlines()
    for line in file_lines:
        if name in line:
            user_doesnotexist = False
            numbers = re.findall(r'\d+', line)
            score = int(numbers[0])


if user_doesnotexist:
    with open("res.txt", 'a') as file:
        if file_lines == 0:
            file.write(f"{name}: ")
        else:
            file.write(f"\n {name}: ")

weapons = input("Choose your weapon >")
weapons = weapons.split(", ")
if len(weapons) > 1:
    user_actions = user_actions + weapons

while exit_game == False:
    def game_cycle():
        global score
        global exit_game
        if len(weapons) == 1:
            game = Game(input(">"), None, ["rock", "paper", "scissors"], None)
        else:
            game = Game(input(">"), None, weapons, None)
        if not any(i in game.user_figure for i in user_actions):
            print("Invalid input!")
            game_cycle()
        else:
            if game.user_figure == "!exit":
                with open("res.txt", 'r') as file:
                    lines = file.readlines()
                    counter = 0
                    for line in lines:
                        if name in line:
                            lines[counter] = name + ": " + str(score)
                        counter += 1
                    file.close()
                '''with open("res.txt", 'w') as file:
                    file.write(''.join(lines))
                    file.close()'''
                print("Bye!")
                exit_game = True
                return
            if game.user_figure == "!rating":
                rating()
            else:
                if len(weapons)>1:
                    counters = weapons[weapons.index(game.user_figure) + 1:]
                    counters += weapons[:weapons.index(game.user_figure)]
                    counters = counters[:len(counters) // 2]
                    if game.bot_figure in counters:
                        print(f"Sorry, but the computer chose {game.bot_figure}")
                    elif game.user_figure == game.bot_figure:
                        print(f"There is a draw ({game.bot_figure})")
                        score += 50
                    else:
                        print(f"Well done. The computer chose {game.bot_figure} and failed")
                        score += 100
                else:
                    if not game.winner_figure():
                        score += 50
                        print(f"Draft! The computer have chosen: {game.bot_figure}")
                    elif game.winner_figure() == "bot":
                        print(f"Computer wins, choosing {game.bot_figure}")
                    elif game.winner_figure() == "user":
                        score += 100
                        print(f"You win, the computer have choosen {game.bot_figure}")
    game_cycle()