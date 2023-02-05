import discord
import json

class ServerCreator:
    def __init__(self, bot, guild):
        self.bot = bot
        self.guild = guild
        
    """
    Function to create categories and channels from given dict
    """
    async def create_categories_and_channels(self):
        guild = self.bot.get_guild(self.guild)
        print(guild)
        with open('./features/creator/channels.json', 'r') as f: 
            categories_channels_dict = json.load(f)
            categories = categories_channels_dict['categories'] 
            for cat in categories:
                category = await guild.create_category(cat['category_name'])
                channels = cat['channels']
                for chan in channels:
                    await guild.create_text_channel(chan['channel_name'], category=category)

    """
    Function to create roles from given dict
    """
    async def create_roles(self):
        guild = self.bot.get_guild(self.guild)
        with open('./features/creator/roles.json', 'r') as f: 
            roles_dict = json.load(f)
            roles = roles_dict['roles']
            for role in roles:
                perms = discord.Permissions(permissions=role['permission_code'])
                await guild.create_role(name=role['role_name'], permissions=perms)

