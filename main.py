import os

import discord
from discord.ext import commands 
from dotenv import load_dotenv
import requests

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
url_status = os.getenv('URL_STATUS')
url_on = os.getenv('URL_ON')
url_off = os.getenv('URL_OFF')


client = commands.Bot(command_prefix = "." ,intents=discord.Intents.all())

class OnButton(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)
    @discord.ui.button(label="server on",style=discord.ButtonStyle.green)
    async def on_button(self,interaction:discord.Interaction,button:discord.ui.Button,):
        requests.post(url_on)
        await interaction.response.edit_message(content=f"The server is turning on")
    

class OffButton(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)
    @discord.ui.button(label="server off",style=discord.ButtonStyle.red)
    async def off_button(self,interaction:discord.Interaction,button:discord.ui.Button,):
        requests.post(url_off)
        await interaction.response.edit_message(content=f"The server is turning off")

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_presence_update(before, after):
    
    if str(after.status) == "online":
        response = requests.get(url_status)
        response_boolean = True if response.text=="True" else False
        
        status = "on" if response_boolean else "off"  
        button = OnButton() if not response_boolean else OffButton()
        
        await after.send(f"The server is currently {status}. Do you want to turn it {'on' if not response_boolean else 'off'}?",view=button)


client.run(TOKEN)