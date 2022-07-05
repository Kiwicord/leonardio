import discord
from discord.ext import commands
from db import *

class DB(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def db(self, ctx):
        post_count = bank.count_documents({})
        await ctx.send(post_count)

async def setup(client):
    await client.add_cog(DB(client))