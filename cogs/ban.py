import discord
from discord.ext import commands

class Ban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member=None, *, reason='Kein Grund angegeben'):
        role = discord.utils.find(lambda r: r.name == '│📋 × Moderator', ctx.message.guild.roles)

        if member is None:
            error = discord.Embed(color=0xE74C3C, title=f'Gib den User an der gebannt werden soll!')
            await ctx.reply(embed=error, mention_author=False)
            return

        if role in member.roles:
            error = discord.Embed(color=0xE74C3C, title=f'Stop!', description=f'Du kannst {member.mention} nicht bannen!')
            await ctx.send(embed=error)
            return

        if member == ctx.author:
            error = discord.Embed(color=0xE74C3C, title=f'Du kannst dich selber nicht bannen!')
            await ctx.send(embed=error)
            return
        embed1 = discord.Embed(color=0xE74C3C, title='Gebannt!', description=f'Der Member {member.mention} wurde von {ctx.author.mention} gebannt.')
        await member.ban(reason=reason)
        await ctx.reply(embed=embed1, mention_author=False)

def setup(client):
    client.add_cog(Ban(client))