import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from features.creator.functions import ServerCreator
from features.music.functions import Music

""" ===== Load info and create client ===== """
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
guild = int(os.getenv('DISCORD_GUILD'))
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


""" ===== Add class features to main program ===== """

creator = ServerCreator(bot, guild)
music = Music(bot)


@bot.event
async def on_message(message):
    if message.author == bot.user:
            return
    
    await bot.process_commands(message)

    if message.content == 'hello':
        await message.channel.send("Hi there!")


@bot.command()
async def create(ctx, arg):
    if arg == 'channels':
        await creator.create_categories_and_channels() 
        await ctx.send('Channels successfully created!')   
    elif arg == 'roles':
        await creator.create_roles()
        await ctx.send('Roles successfully created!')


@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)

@bot.command()
async def gif(ctx, arg):
    await ctx.send(embed=discord.Embed().set_image(url=arg))


""" ===== Add class features to main program ===== """
bot.run(token)