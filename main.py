import time, telepot, random
import bots
from settings import TOKEN

bot_list = [bots.DogeKunBot(), bots.JaevBot(), bots.DiggoBot()]

def handle(msg):
    # Message info
    #content_type, chat_type, chat_id = telepot.glance(msg)

    # Random bot response if it's ready to act
    random_bot = random.choice(bot_list)
    if random_bot.check():
        random_bot.act(msg, bot)

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
	time.sleep(10)
