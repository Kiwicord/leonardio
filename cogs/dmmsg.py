import discord
from discord.ext import commands

class DmMsg(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def msg(self, ctx, member:discord.Member, *, reason=None):
        embed1 = discord.Embed(title='**MSG**', description=f'Narchicht wurde an **{member}** gesendet.', color=0xE74C3C)
        embed1.add_field(name="MSG:", value=f"{reason}")
        embed2 = discord.Embed(title='**MSG**', description=f'MSG von **{member.mention}**:', color=0xE74C3C)
        embed2.add_field(name="MSG:", value=f"{reason}")
        await ctx.reply(embed=embed1)
        await member.send(embed=embed2)

def setup(client):
    client.add_cog(DmMsg(client))