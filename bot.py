import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from features.creator.functions import ServerCreator
from features.music.functions import Music

""" ===== Load info and create client ===== """
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
guild = os.getenv('DISCORD_GUILD')
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


""" ===== Add class features to main program ===== """

creator = ServerCreator(bot)
music = Music(bot)


@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == guild:
            break

    # await creator.create_roles(guild)
    # await creator.create_categories_and_channels(guild) 

@bot.event
async def on_message(message):
    if message.author == bot.user:
            return
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)
    # print(username)
    # print(user_message)
    # print(channel)
    if message.content == 'hello':
        await message.channel.send("Hi there!")


""" ===== Add class features to main program ===== """
bot.run(token)