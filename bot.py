import os
import discord
from dotenv import load_dotenv
from features.creator.functions import ServerCreator
from features.music.functions import Music

""" ===== Load info and create client ===== """
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
guild = os.getenv('DISCORD_GUILD')
client = discord.Client(intents=discord.Intents.default())


""" ===== Add class features to main program ===== """

creator = ServerCreator(client, guild)
music = Music(client)


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == guild:
            break

    # await creator.create_roles()
    # await creator.create_categories_and_channels() 

@client.event
async def on_message(message):
    if message.content == 'hello':
        await message.channel.send("Hi there!")
        

""" ===== Add class features to main program ===== """
client.run(token)