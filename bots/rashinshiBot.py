#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telepot
import random
from libs.bot import Bot

class RashinshiBot(Bot):

    # Initializing variables
    def __init__(self):
        self.DCC_reference = "rachinski"
        self.question = ''
        self.holding_question = False
        self.msg_counter = 0
        self.max_counter = 100 # message delay

    # Defining act function
    def act(self, msg, bot):
        # How to get info of the message
        content_type, chat_type, chat_id = telepot.glance(msg)
        bot.sendMessage(chat_id, self.DCC_reference + ' : cabros, ' + self.question)
        # Resetting data
        self.question = ''
        self.holding_question = False
        self.msg_counter = 0

    # Defining check function
    def check(self):
        # ready to act after x number of messages
        if self.msg_counter >= self.max_counter and self.holding_question:
            return True
        else:
            return False

    # Defining newMessageHandler function
    def newMessageHandler(self, msg):
        # Try to hold a question and start counting all the messages
        if not self.holding_question:
            content_type, chat_type, chat_id = telepot.glance(msg)
            if content_type == 'text':
                if msg['text'].endswith('?'):
                    self.question =  msg['text']
                    self.holding_question = True
        else:
            self.msg_counter += 1
