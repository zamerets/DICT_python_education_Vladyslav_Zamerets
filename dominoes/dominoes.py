import random

domino = [[i, j] for i in range(7) for j in range(i, 7)]


random.shuffle(domino)
stock_pieces = domino[:14]
bot = domino[14:21]
player = domino[21:]

snake = max(max(bot), max(player))

if snake in bot:
    bot.remove(snake)
    status = 'player'
else:
    player.remove(snake)
    status = 'bot'

print("="*150)
print("Stock pieces:", stock_pieces)
print("Computer pieces:", bot)
print("Player pieces:", player)
print("Domino snake:", [snake])
print("Game status:", status)