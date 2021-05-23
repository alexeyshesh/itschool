import telebot
import config
from telebot.types import ReplyKeyboardMarkup
import requests
import time

# Создаем бота
bot = telebot.TeleBot(config.token)

users = {}


@bot.message_handler(commands=['start'])
def start(message):
    text = "Привет! Я бот, который знает погоду. Из какого ты города?"
    bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(message, get_city)


def get_city(message):
    username = message.from_user.username

    if message.text.lower() in config.city_codes:
        if username not in users:
            users[username] = [ config.city_codes[message.text.lower()] ]
        else:
            users[username].append(config.city_codes[message.text.lower()])
    else:
        bot.reply_to(message, "Погода в этом городе недоступна. Введите другой город.")
        bot.register_next_step_handler(message, get_city)

    keyboard = ReplyKeyboardMarkup(True, False)
    keyboard.row(config.get_weather_label)
    bot.send_message(message.chat.id,
                     "Запомнил!",
                     reply_markup=keyboard)


def get_weather(q):
    query = config.querystring.copy()
    query['q'] = q
    response = requests.request("GET", config.url, headers=config.headers, params=query)
    return response.json()


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text == config.get_weather_label:
        answer  = ""
        for city in users[message.from_user.username]:
            weather = get_weather(users[message.from_user.username])
            text = "[{}] На улице {}, температура {}ºС, ощущается как {}ºC, влажность - {}%".format(
                weather['name'],
                weather['weather'][0]['description'],
                weather['main']['temp'],
                weather['main']['feels_like'],
                weather['main']['humidity']
            )
            answer += text + '\n\n'
        bot.send_message(message.chat.id, answer)


if __name__ == "__main__":
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(e)
            time.sleep(10)