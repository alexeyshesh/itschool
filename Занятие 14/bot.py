import discord
import requests
import re
from discord.ext import commands
import youtube_dl
import os

client = commands.Bot(command_prefix='!')

@client.command()
async def play(ctx, url):
    # !play youtube.com/song
    song_there = os.path.isfile('song.mp3')
    if song_there:
        os.remove('song.mp3')

    voice_channel = discord.utils.get(ctx.guild.voice_channels, name='Основной')
    await voice_channel.connect()

    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    for file in os.listdir('./'):
        if file.endswith('.mp3'):
            os.rename(file, 'song.mp3')

    voice.play(discord.FFmpegPCMAudio('song.mp3'))


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()

@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send('Я не в голосовом канале')

client.run('TOKEN')
