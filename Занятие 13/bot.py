import discord
import requests
import json
from googletrans import Translator


TOKEN = 'TOKEN'
t = Translator()
client = discord.Client()


@client.event
async def on_ready():
    print('We are connected')


def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    data = json.loads(response.text)
    return t.translate('{} ({})'.format(data[0]['q'], data[0]['a']), dest='ru').text


@client.event
async def on_message(message):
    print(message)
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hi!')

    if message.content.startswith('?'):
        await message.channel.send(get_quote())


client.run(TOKEN)