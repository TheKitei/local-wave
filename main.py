import discord
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('CLIENT_TOKEN')


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Ping'):
        await message.channel.send('pong')

client.run(token)

