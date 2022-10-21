import discord
from discord.ext import commands

class Custom(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['c'])
    async def custom(self, ctx, *, txt):
        await ctx.message.delete()
        await ctx.send(txt)
        

async def setup(client):
    await client.add_cog(Custom(client))