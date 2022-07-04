import discord
from discord.ext import commands
from db import *

class Deposit(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.err = ''

    @commands.command(aliases=['dep', 'Deposit', 'DEP', 'Dep'])
    async def deposit(self, ctx, amount=None):
        wallet_amt = await get_wallet(ctx.author.id)
        err_embed = discord.Embed(color=0xE74C3C, title='')
        if amount is None:
            err_embed.title = '✨🧨 Bitte gib den Betrag an!'
            await ctx.reply(embed=err_embed, mention_author=False)
            return

        if amount == 'all':
            amount = int(wallet_amt)
            if wallet_amt <= 0:
                embed_not_enough_money = discord.Embed(color=0xE74C3C, title='✨🧨 Du hast nicht genügend Geld!')
                await ctx.reply(embed=embed_not_enough_money, mention_author=False)
                return

        if wallet_amt < int(amount):
            embed_not_enough_money = discord.Embed(color=0xE74C3C, title='✨🧨 Du hast nicht genügend Geld!')
            await ctx.reply(embed=embed_not_enough_money, mention_author=False)
            return
        
        embed = discord.Embed(color=0xE74C3C, title='✨🧨 Überwiesen!', description=f'Du hast erfolgreich **{int(amount):,}**🥝 auf deine Bank überwiesen!')
        await open_profile(ctx.author.id)
        await deposit_amt(ctx.author.id, amount=int(amount))
        await ctx.reply(embed=embed, mention_author=False)

async def setup(client):
    await client.add_cog(Deposit(client))