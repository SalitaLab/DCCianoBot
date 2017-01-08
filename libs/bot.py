# Class for bots

# If you want to add a bot:
#   1- Create a bot.py class inside de bots folder
#   2- Import bot into bots/__init__.py
#   3- Add the bot to the array inside main.py

# ****** Remember that your bot MUST implement the check and act methods ******
class Bot:
    #init bot
    def __init__(self):
        return

    # Implement this method like a 'handle' method from a telepot bot, use bots/DogeKunBot.py as reference. This method is called randomly between all available bots.
    def act(self, msg, bot):
        return

    # If check returns true then the bot will call the act method. False means that the bot isnt ready to act. This method is called randomly between all available bots.
    def check(self):
        return

    # This function will be called everytime the Main bot receives a message in case you want to hold information to use in the future.
    # You are not supposed to send message in this method.
    def newMessageHandler(self, msg):
        return

    # Gets the mutex of main.py
    def lock(self):
        # TODO implementation
        return

    # Releases the mutex of main.py
    def unlock(self):
        # TODO implementation
        return
