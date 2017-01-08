import time, telepot, random
import bots
from settings import TOKEN

bot_list = [bots.DogeKunBot(), bots.JaevBot(), bots.DiggoBot()]

def handle(msg):
    # Message info
    content_type, chat_type, chat_id = telepot.glance(msg)

    # Return send bot response
    random.choice(bot_list).act(msg, bot)

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
	time.sleep(10)
