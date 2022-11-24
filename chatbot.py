from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot("Talker")

training = ChatterBotCorpusTrainer(bot)
training.train("chatterbot.corpus.english.conversations")

exit_commands = ("quit", "exit", "bye")

while True:
    user_query = input("? ")
    if user_query in exit_commands:
        break
    else:
        print(f":) {bot.get_response(user_query)}")
