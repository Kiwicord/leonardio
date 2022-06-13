import discord
from discord.ext import commands

class Del(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        bad_words = ['fuck', 'pay day']
        msg = message.content
        if msg in bad_words:
            await message.delete()

def setup(client):
    client.add_cog(Del(client))