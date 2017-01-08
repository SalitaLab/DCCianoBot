import telepot
import random
from libs.bot import Bot

class JaevBot(Bot):

    # Initializing variables
    def __init__(self):
        self.DCC_reference = "jaev"
        self.comida = ["papa juan", "completos", "hamburguesas", "pizzas", "sushi", "shawarma", "con la familia", "papas fritas"]

    # Defining act function
    def act(self, msg, bot):
        # How to get info of the message
        content_type, chat_type, chat_id = telepot.glance(msg)
        bot.sendMessage(chat_id, self.DCC_reference + ' : aki io comiendo ' + random.choice(self.comida))

    # Defining readyToAct function
    def readyToAct(self):
        return True #Always ready to act
