import os

import discord
from dotenv import load_dotenv
import requests

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
url_on = os.getenv('URL_ON')
url_off = os.getenv('URL_OFF')

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'server on':
        requests.post(url_on)
        await message.channel.send('server is turning on')
    if message.content == 'server off':
        requests.post(url_off)
        await message.channel.send('server is turning off')
        

client.run(TOKEN)