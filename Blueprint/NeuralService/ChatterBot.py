'''
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot(	'Norman',
				silence_performance_warning=True
				)

bot.set_trainer(ChatterBotCorpusTrainer)
bot.train("chatterbot.corpus.english")
'''