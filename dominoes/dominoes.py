import random


domino = [[i, j] for i in range(7) for j in range(i, 7)]
random.shuffle(domino)
stock = domino[:14]
bot = domino[14:21]
player = domino[21:]

snake = max(max(bot), max(player))

if snake in bot:
    bot.remove(snake)
    status = 'player'
else:
    player.remove(snake)
    status = 'bot'

print('=' * 120)
print("Stock size:", len(stock))
print("Computer pieces:", len(bot))
print()
print(snake)
print()
print("Your pieces:")
for i in range(len(player)):
    n = i + 1
    pieces = player[i]
    print("{}:{}".format(n, pieces))

if status == 'player':
    print()
    print("Status: It's your turn to make a move. Enter your command.")
else:
    print()
    print("Status: Computer is about to make a move. Press Enter to continue...")



