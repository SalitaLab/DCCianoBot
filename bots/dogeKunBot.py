#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telepot
import random
from libs.bot import Bot

class DogeKunBot(Bot):

    # Initializing variables
    def __init__(self):
        self.DCC_reference = "doge"
        self.frases = ['/legalicenalasde15', 'el problema es que soy gay', 'esta mas muerto que la tula de jaime guzman', 'si no la probay como vay a saber si te gusta', 'porque la tengo chica, por eso',
        'esa huea es de maricones po', 'oye comi, eri pan-fleto?', 'sabias que la vaca babea mas de 100 litros por dia?', 'sono toori da', 'そのとおりです。', 'y tu mama conchetumadre? tu mama tmb es un bot',
        'mami no le di color, empresta loh kcht', 'es que varas es autonomo, por eso trabaja gratis', 'las polillas son fuente de nutrientes', 'lo dije una vez que estaba muy curado', 'naru hodo', 'Como esos monos chinos qls gays?',
        'ahhh! se escucha como la tula!', 'ambar con tula o hiho con vagina?', 'pero que paja esa weaaaaa', 'estoy hecho concha wn', 'te pusiste fleto wn, la cagai', 'puta la weona feminazi... me triguereai', 'y si me pesco a tu mama?', 'el sexo anal no es sexo',
        'aweonao conchetumare', 'aborto ajajaj que buen apellido', 'menos mal voté por la une', 'mi familia es evangelica y no cree en la evolucion', 'Curao si, curiao no', 'No me gustan los panes :(']

    # Defining act function
    def act(self, msg, bot):
        # How to get info of the message
        content_type, chat_type, chat_id = telepot.glance(msg)
        bot.sendMessage(chat_id, self.DCC_reference + ' : ' + random.choice(self.frases), reply_to_message_id=msg['message_id'])

    # Defining readyToAct function
    def readyToAct(self):
        return True #Always ready to act
