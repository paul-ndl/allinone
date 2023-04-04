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
bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())


""" ===== Add class features to main program ===== """

@bot.event
async def on_ready():
    await bot.add_cog(ServerCreator(bot))
    await bot.add_cog(Music(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
            return
    
    await bot.process_commands(message)


""" ===== Add class features to main program ===== """
if __name__ == "__main__":
    bot.run(token)