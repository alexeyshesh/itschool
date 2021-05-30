import telebot
import config
from PIL import Image, ImageDraw, ImageFont
import random

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=['photo'])
def get_image(message):
    photo = message.photo[-1]
    file_info = bot.get_file(photo.file_id)
    file = bot.download_file(file_info.file_path)
    with open('image.jpg', 'wb') as f:
        f.write(file)

    text = config.captures[random.randint(0, len(config.captures) - 1)]
    font = ImageFont.truetype('lobster.ttf', size=min(100, (photo.width - 60) // max([len(s) for s in text.split('\n')]) * 2))
    text_width, text_height = font.getsize(text)
    img = Image.open('image.jpg')
    draw = ImageDraw.Draw(img)

    text_y = photo.height - text_height * len(text.split('\n')) - 30
    for line in text.split('\n'):
        text_width, text_height = font.getsize(line)
        draw.text(((photo.width - text_width) // 2 + 2, text_y + 2), line, 'black', font)
        draw.text(((photo.width - text_width) // 2, text_y), line, 'white', font)
        text_y += text_height

    img.save('image1.jpg')

    bot.send_photo(message.chat.id, open('image1.jpg', 'rb'))

if __name__ == "__main__":
    bot.polling(none_stop=True)