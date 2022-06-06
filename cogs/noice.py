import discord
from discord.ext import commands

class Noice(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        msg = message.content
        for word in msg:
            if msg.find('noice') != -1:
                await message.delete()
                return 

def setup(client):
    client.add_cog(Noice(client))