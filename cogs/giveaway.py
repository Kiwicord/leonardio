import discord
from discord.ext import commands
import asyncio
import random
import datetime

class Giveaway(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['g', 'G', 'Give', 'give'])
    async def giveaway(self, ctx, time:int=None, *, price:str=None):
        #if ctx.author.mention == 745717254678904862:
        #    return
        if price is None:
            error = discord.Embed(color=0xE74C3C, title='Error!', description='Bitte geben sie einen **Preis** an.')
            await ctx.send(embed=error)
            return
        if time is None:
            error = discord.Embed(color=0xE74C3C, title='Error!', description='Bitte geben sie eine **Dauer** an an.')
            await ctx.send(embed=error)
            return
            
        seconds = time

        hours = int(seconds / 3600)
        minutes = int(seconds / 60)
        days = int(hours / 24)

        if hours > 24:
            embed1 = discord.Embed(color=0xE74C3C, title=':tada:Giveaway!:tada:', description=f'Preis: **{price}**\nZeit: **{days}** tag(e)\nSponsor: **{ctx.author.mention}**')
            msg1 = await ctx.send(embed=embed1)
            await msg1.add_reaction('🎉')
            await asyncio.sleep(time)

            msg1 = await ctx.channel.fetch_message(msg1.id)
            players = await msg1.reactions[0].users().flatten()
            players.pop(players.index(self.client.user))
            winner = random.choice(players)

            await ctx.send(winner)

            return
        if time > 3600:
            embed2 = discord.Embed(color=0xE74C3C, title=':tada:Giveaway!:tada:', description=f'Preis: **{price}**\nZeit: **{hours}** stunde(n)\nSponsor: **{ctx.author.mention}**')
            msg2 = await ctx.send(embed=embed2)
            await msg2.add_reaction('🎉')
            await asyncio.sleep(time)

            msg2 = await ctx.channel.fetch_message(msg2.id)
            players = await msg2.reactions[0].users().flatten()
            players.pop(players.index(self.client.user))
            winner = random.choice(players)

            await ctx.send(winner)

            return
        if time > 60:
            embed3 = discord.Embed(color=0xE74C3C, title=':tada:Giveaway!:tada:', description=f'Preis: **{price}**\nZeit: **{minutes}** Minute(n)\nSponsor: **{ctx.author.mention}**')
            msg3 = await ctx.send(embed=embed3)
            await msg3.add_reaction('🎉')
            await asyncio.sleep(time)

            msg3 = await ctx.channel.fetch_message(msg3.id)
            players = await msg3.reactions[0].users().flatten()
            players.pop(players.index(self.client.user))
            winner = random.choice(players)

            await ctx.send(winner)

            return
        if time > 0:
            embed4 = discord.Embed(color=0xE74C3C, title=':tada:Giveaway!:tada:', description=f'Preis: **{price}**\nZeit: **{seconds}** Sekunde(n)\nSponsor: **{ctx.author.mention}**')
            msg4 = await ctx.send(embed=embed4)
            await msg4.add_reaction('🎉')
            await asyncio.sleep(time)

            msg4 = await ctx.channel.fetch_message(msg4.id)
            players = await msg4.reactions[0].users().flatten()
            players.pop(players.index(self.client.user))
            winner = random.choice(players)

            await ctx.send(winner)

            return



async def setup(client):
    await client.add_cog(Giveaway(client))