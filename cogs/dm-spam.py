import discord
from discord.ext import commands

class DmSpam(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def dmspam(self, ctx, member:discord.Member):
        embed1 = discord.Embed(title='**SPAM**', description=f'{member} wird **Angespamt**.', color=0xE74C3C)
        embed2 = discord.Embed(title='**SPAM**', description=f'SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM .', color=0xE74C3C)
        await ctx.reply(embed=embed1)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        await member.send(embed=embed2)
        

def setup(client):
    client.add_cog(DmSpam(client))