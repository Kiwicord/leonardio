import discord
from discord.ext import commands
from db import *

class Ad(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def ad(self, ctx, member:discord.Member, *, amount=None):
        amount = int(amount)
        if amount is None:
            error = discord.Embed(color=0xE74C3C, title=f'🧨✨ Bitte gib den Betrag an!')
            await ctx.send(embed=error)
            return
        if member is None:
            embed = discord.Embed(color=0xE74C3C, title=f'🧨✨ DU HATATATATST {amount} 🧨 zu deinem Wallet hinzugefügt')
            await open_profile(ctx.author.id)
            await update_wallet(ctx.author.id, amount)
            await ctx.reply(embed=embed)
        else:
            embed = discord.Embed(color=0xE74C3C, title=f'🧨✨ DU HATATATATST {amount} 🧨 zu {member} Wallets hinzugefügt')
            await open_profile(member.id)
            await update_wallet(member.id, amount)
            await ctx.reply(embed=embed)

async def setup(client):
    await client.add_cog(Ad(client))