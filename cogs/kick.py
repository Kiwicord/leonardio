import discord
from discord.ext import commands

class Kick(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason=None):

        if member:
            guild = ctx.guild

            await member.send(f'Du wurdest von **{guild.name}** geckickt | Grund: **{reason}**')
            await member.kick(reason=reason)
            embed1 = discord.Embed(color=0xE74C3C, title='Geckickt!', description=f'Der Member {member.mention} wurde von {ctx.author.mention} Geckickt. Grund: {reason}')
            await ctx.reply(embed=embed1, mention_author=False)
        else:
            error = discord.Embed(color=0xE74C3C, title=f'Stop!', description=f'Du kannst {member.mention} nicht kicken! DU MONG DB')
            await ctx.send(embed=error)
            return

def setup(client):
    client.add_cog(Kick(client))