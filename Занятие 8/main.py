import telebot
import config
import time

# Создаем бота
bot = telebot.TeleBot(config.token)

users = {}

# функция, которая будет выполняться при отправке команды /start
@bot.message_handler(commands=['start'])
def start(message):
    text = "Привет! Как тебя зовут?"
    bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(message, get_name)  # следующая функция в цепи 
                                                       # сообщений

def get_name(message):
    name = message.text
    username = message.from_user.username
    users[username] = {}
    users[username]['name'] = name
    text = "Сколько тебе лет?"
    bot.reply_to(message, text)
    bot.register_next_step_handler(message, get_age)


def get_age(message):
    username = message.from_user.username
    if message.text.lower() == "не скажу":
        bot.reply_to(message, 'Ладно( Не запомню тебя')
        del users[username]
        return
    if not message.text.isdecimal():
        bot.reply_to(message, "Не понимаю, можно цифрами?")
        bot.register_next_step_handler(message, get_age)
    else:
        users[username]['age'] = message.text
        text = "Хорошо, я тебя запомню!"
        bot.reply_to(message, text)


# функция, котоорая выпполняется при отправке текстового сообщения
@bot.message_handler(content_types=['text'])
def answer(message):
    username = message.from_user.username
    if message.text.lower() == "кто я?":
        if username in users:
            name = users[username]['name']
            age = users[username]['age']
            bot.reply_to(message, "Тебя зовут {}, тебе {} лет".format(name, age))
        else:
            text = "Я не знаю, кто ты. Как тебя зовут?"
            bot.reply_to(message, text)
            bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.chat.id, message.text)


if __name__ == "__main__":
    while True:
        try:
            bot.polling(none_stop=True)  # запуск бота
        except Exception as e: # если что-то пошло не так, ошибка сохранится в e
            print(e)
            time.sleep(10)  # после оошибки останавливаем бота на 10 секунд