import discord
from discord.ext import commands
from db import *

class Ad(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def ad(self, ctx, amount=None):
        amount = int(amount)
        if amount is None:
            error = discord.Embed(color=0xE74C3C, title=f'🧨✨ Bitte gib den Betrag an!')
            await ctx.send(embed=error)
            return
        else:
            await open_profile(ctx.author.id)
            await update_wallet(ctx.author.id, amount)

async def setup(client):
    await client.add_cog(Ad(client))