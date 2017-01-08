# Main Class for bots

# If you want to add a bot:
#   1- Create a bot.py class inside de bots folder
#   2- Import bot into bots/__init__.py
#   3- Add the bot to the array inside main.py

# ****** Remember that your bot MUST implement the check and act methods ******
class Bot:
    #init bot
    def __init__(self):
        return

    # Implement this method like a handle method from a telepot bot, use bots/DogeKunBot.py as reference
    def act(self, msg, bot):
        return

    # If check returns true then the bot will call the act method. False means that the bot isnt ready to act.
    def check(self):
        return

    # Gets the mutex of main.py
    def lock(self):
        # TODO implementation
        return

    # Releases the mutex of main.py
    def unlock(self):
        # TODO implementation
        return
