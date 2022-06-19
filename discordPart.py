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


    user = message.author.discriminator
    friend = User(user)


    if message.content == "help":
         await message.channel.send("Welcome to locale wave!\nMy current commands!\n")
         await message.channel.send("1.To add location to your list use | add location {location1} {location2} ...|")
         await message.channel.send("2. Recive event list |Force| ")




    if message.content.startswith('add location'):

        locations = (message.content.replace("add location","")).split()
        friend.addLoc(locations)
        
        await message.channel.send('Done!😉')

    if message.content.startswith('force'):
        freindEvent = friend.sendEvents()

        for i in range(len(freindEvent)):
            
            await message.channel.send( freindEvent[i][1])
            embed = discord.Embed()
            embed.description = (('\n❗' +freindEvent[i][0] + '❗' + '\n' +'Where📍?:' +freindEvent[i][2] + '\n' + 'When⏰?:' + freindEvent[i][3] + '\nCheck it out🌐!:' + '[Here]({link})').format(link = freindEvent[i][4]))
            await message.channel.send( embed=embed)
            time.sleep(0.5)
        





client.run(token)

