import os
import discord
import json
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=discord.Intents.default())

async def create_categories_and_channels(guild, categories_channels_dict : dict):
    categories = categories_channels_dict['categories'] 
    for cat in categories:
        category = await guild.create_category(cat['category_name'])
        channels = cat['channels']
        for chan in channels:
            await guild.create_text_channel(chan['channel_name'], category=category)

async def create_roles(guild, roles_dict : dict):
    roles = roles_dict['roles']
    for role in roles:
        perms = discord.Permissions(permissions=role['permission_code'])
        await guild.create_role(name=role['role_name'], permissions=perms)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    with open('roles.json', 'r') as f: 
        roles_dict = json.load(f)
        await create_roles(guild, roles_dict) 

    """with open('channels.json', 'r') as f: 
        categories_channels_dict = json.load(f)
        await create_categories_and_channels(guild, categories_channels_dict)"""

client.run(TOKEN)
