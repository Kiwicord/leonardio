import discord
from discord.ext import commands

class Clear(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.has_permissions(ban_members=True)
    @commands.command(aliases=['purge', 'p'])
    async def clear(self, ctx, amount : int):
        print(f'{ctx.author.display_name} hat clear ausgefürt.')
        await ctx.channel.purge(limit=amount+1)

async def setup(client):
    await client.add_cog(Clear(client))