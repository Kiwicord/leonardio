import discord
from discord.ext import commands

class Rules(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def newrule(self, ctx):
        
            
async def setup(client):
    await client.add_cog(Rules(client))