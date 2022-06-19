import discord
import os
from dotenv import load_dotenv
import time
from userObj import User


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
# add location or add?
    # message.content = str
    user = message.author.discriminator
    friend = User(user)


    if message.content.startswith('add location'):

        locations = (message.content.replace("add location","")).split()
        friend.addLoc(locations)
        
        await message.channel.send('pong')

    if message.content.startswith('foo'):
        freindEvent = friend.sendEvents()

        for i in range(len(freindEvent)):
            await message.channel.send('-------------- \n' +freindEvent[i][1] + '\n')
            time.sleep(0.5)
            await message.channel.send('' +freindEvent[i][1] + '\n')
            await message.channel.send(freindEvent[i][0] + '\n')
        





client.run(token)

