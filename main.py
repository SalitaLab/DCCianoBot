import time, telepot, random
import bots
from settings import TOKEN

bot_list = [bots.DogeKunBot(), bots.JaevBot(), bots.DiggoBot(), bots.RashinshiBot()]

def handle(msg):
    # Message info
    # content_type, chat_type, chat_id = telepot.glance(msg)

    # new message received, calling newMessageHandler for everyone
    for _bot in bot_list:
        _bot.newMessageHandler(msg)


    random.shuffle(bot_list)
    for random_bot in bot_list:
        # Random bot response if it's ready to act
        if random_bot.check():
            random_bot.act(msg, bot)
            break

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
	time.sleep(10)
