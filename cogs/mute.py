import discord
import DateTime
import humanfriendly
from discord.ext import commands
from datetime import datetime, timedelta

class Mute(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def mute(self, ctx, member : discord.Member=None, time=None, *, reason=None):
        if ctx.author.id == 977993035717681252:
            guild = ctx.guild

            time = humanfriendly.parse_timespan(time)
            await member.timeout(until = discord.utils.utcnow() + timedelta(seconds=time), reason=reason)
            embed1 = discord.Embed(color=0xE74C3C, title='Gemutet!', description=f'Der Member {member.mention} wurde von {ctx.author.mention} für {time} sekunden Gemutet. Grund: **{reason}**')
            await ctx.reply(embed=embed1, mention_author=False)
            await member.send(f'Du wurdest auf **{guild.name}** gemutet. | Grund: **{reason}**')
        else:
            error = discord.Embed(color=0xE74C3C, title=f'Stop!', description=f'Du kannst {member.mention} nicht muten! DU MONG DB')
            await ctx.send(embed=error)
            return
    
    @commands.command()
    async def unmute(self, ctx, member : discord.Member=None, time=None):

        if ctx.author.id == 977993035717681252:
            guild = ctx.guild

            await member.timeout(until = None)
            embed2 = discord.Embed(color=0xE74C3C, title='Gemutet!', description=f'Der Member {member.mention} wurde von {ctx.author.mention} Entmutet.')
            await ctx.reply(embed=embed2, mention_author=False)
            await member.send(f'Du wurdest auf **{guild.name}** entmutet.')
        else:
            error = discord.Embed(color=0xE74C3C, title=f'Stop!', description=f'Du kannst {member.mention} nicht unmuten! DU MONG DB')
            await ctx.send(embed=error)
            return
        


def setup(client):
    client.add_cog(Mute(client))