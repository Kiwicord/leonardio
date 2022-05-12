import discord
from discord.ext import commands

class Ban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        if ctx.author.id == 712341730480881707:
            await member.ban(reason=reason)
            await ctx.reply(f'{member.mention} wurde von diesem Server gebannt')

def setup(client):
    client.add_cog(Ban(client))