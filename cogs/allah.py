import discord
from discord.ext import commands
import random
import pymongo
from pymongo import MongoClient

class Test(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def allah(self, ctx):
        if ctx.author.id == 745717254678904862:
            embed = discord.Embed(title= '', description= 'NOT ANY MORE', color=0xE74C3C)
            await ctx.send(embed=embed)
        else:
            print('sus')
            
async def setup(client):
    await client.add_cog(Test(client))