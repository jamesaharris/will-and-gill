from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

william = ChatBot('WILLIAM')
gilbert = ChatBot('GILBERT')

# Create a new trainer for the chatbot
trainwill = ChatterBotCorpusTrainer(william)
traingill = ChatterBotCorpusTrainer(gilbert)

william.storage.drop()
gilbert.storage.drop()

traingill.train("chatterbot.corpus.english")
traingill.train("chatterbot.corpus.french")
traingill.train("chatterbot.corpus.german")
traingill.train("chatterbot.corpus.spanish")

traingill.train("chatterbot.corpus.english")
traingill.train("chatterbot.corpus.french")
traingill.train("chatterbot.corpus.german")
traingill.train("chatterbot.corpus.spanish")

traingill.train("chatterbot.corpus.english")
traingill.train("chatterbot.corpus.english")

wills = input("Starting string?")
while True:
    print(gilbert.get_response(wills))
    gills = gilbert.get_response(wills)
    print(william.get_response(gills))
    wills = william.get_response(gills)
