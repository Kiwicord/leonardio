import discord
from discord.ext import commands

class Jason(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def jasonisttoll(self, ctx):
        if ctx.author.id == 745717254678904862:
            await ctx.reply('Nah u are not')
        else:
            await ctx.reply('Yeah he is realy nice. LOL')

def setup(client):
    client.add_cog(Jason(client))