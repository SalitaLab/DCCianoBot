# Main Class for bots

# If you want to add a bot:
#   1- Create a bot.py class inside de bots folder
#   2- Import bot into main.py
#   3- Add the bot to the array inside main.py

# ****** Remember that your bot MUST implement the act method ******
class Bot:
    #init bot
    def __init__(self):
        return

    # Gets the mutex of main.py
    def lock(self):
        # TODO implementation
        return

    # Implement this method like a handle method from a telepot bot, use bots/DogeKunBot.py as reference
    def act(self, msg, bot):
        return

    # Releases the mutex of main.py
    def release(self):
        # TODO implementation
        return
