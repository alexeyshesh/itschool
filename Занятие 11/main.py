import telebot
import config
import re

bot = telebot.TeleBot(config.token)

groups = {}

@bot.message_handler(commands=['creategroup'])
def creategroup(message):
    group_name = re.findall('\$\w+', message.text)
    if group_name == []:
        return
    group_name = group_name[0]
    group = re.findall('@[\w\d_]+', message.text)
    groups[group_name] = group
    print(groups)

@bot.message_handler(content_types=['text'])
def text(message):
    mentions = re.findall('\$\w+', message.text)
    if mentions:
        for mention in mentions:
            if mention in groups:
                bot.reply_to(message, ' '.join(groups[mention]))


if __name__ == "__main__":
    bot.polling(none_stop=True)