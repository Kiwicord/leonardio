import discord
import DateTime
import humanfriendly
from discord.ext import commands
from datetime import datetime, timedelta

class Mute(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def mute(self, ctx, member : discord.Member=None, time=None, *, reason=None):
        if member:
            guild = ctx.guild

            time = humanfriendly.parse_timespan(time)
            await member.timeout(until = discord.utils.utcnow() + timedelta(seconds=time), reason=reason)
            embed1 = discord.Embed(color=0xE74C3C, title='Gemutet!', description=f'Der Member {member.mention} wurde von {ctx.author.mention} für {time} sekunden Gemutet. Grund: **{reason}**')
            await ctx.reply(embed=embed1, mention_author=False)
            embed4 = discord.Embed(title='Gemutet!', description=f'Du wurdest auf **{guild.name}** für {time} sekunden gemutet! | Grund: **{reason}**', color=0xE74C3C)
            await member.send(embed=embed4)
        else:
            error = discord.Embed(color=0xE74C3C, title=f'Stop!', description=f'Du kannst {member.mention} nicht muten! DU MONG DB')
            await ctx.send(embed=error)
            return
        print(f'{ctx.author.display_name} hat mute ausgefürt.')
    
    @commands.has_permissions(administrator=True)
    @commands.command()
    async def unmute(self, ctx, member : discord.Member=None):

        if member:
            guild = ctx.guild

            await member.timeout(until = None)
            embed2 = discord.Embed(color=0xE74C3C, title='Gemutet!', description=f'Der Member {member.mention} wurde von {ctx.author.mention} Entmutet.')
            await ctx.reply(embed=embed2, mention_author=False)
            embed3 = discord.Embed(title='Gemutet', description=f'Du wurdest auf **{guild.name}** entmutet.', color=0xE74C3C)
            await member.send(embed=embed3)
        else:
            error = discord.Embed(color=0xE74C3C, title=f'Stop!', description=f'Du kannst {member.mention} nicht unmuten! DU MONG DB')
            await ctx.send(embed=error)
            return
        print(f'{ctx.author.display_name} hat unmute ausgefürt.')
        


async def setup(client):
    await client.add_cog(Mute(client))