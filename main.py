import time
import telepot
import random
from bots import dogeKunBot, jaevBot
from settings import TOKEN

bot_list = [dogeKunBot.DogeKunBot(), jaevBot.JaevBot(), ]

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
