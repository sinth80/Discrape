import discord
from discord.ext import commands
import time

client = discord.Client()
client = commands.Bot(command_prefix="ds ")
print("input bot token")
TOKEN = input()




@client.command()
async def scrape(ctx, channel: discord.TextChannel=None):

    text_channel_list = []
    for guild in client.guilds:
        for channel in guild.text_channels:
            text_channel_list.append(channel)

    textLen = len(text_channel_list)



    arrNum = 0
    for item in range(textLen):

        channel = text_channel_list[arrNum - 1]

        count = 0
        async for _ in channel.history(limit=None):
            count += 1

        messages = await channel.history(limit=count).flatten()

        msgArr = []

        for message in messages:
            msgStat = "name: " + message.author.name + " author id: " + str(message.author.id) + " channel name: " + channel.name + " channel id: " + str(channel.id) + " content: " + message.content
            if message.attachments != 0:
                urlArr = []
                urlNum = 0
                for item in message.attachments:
                    att = message.attachments[urlNum]
                    urlArr.append(att.url)
                    urlNum = urlNum + 1


                msgStat = msgStat + " attachments: " + str(urlArr)
            msgArr.append(msgStat)

            with open(channel.name + '.txt', 'w') as f:
                for item in msgArr:
                    f.write("%s\n" % item)



        f.close()

        arrNum = arrNum + 1







@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
