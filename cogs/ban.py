import discord
from discord.ext import commands

class Ban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason='Kein Grund angegeben'):
        print(f'{ctx.author.display_name} hat ban ausgefürt.')

        guild = ctx.guild

        if member:
            embed1 = discord.Embed(color=0xE74C3C, title='Gebannt!', description=f'Der Member {member.mention} wurde von {ctx.author.mention} gebannt. Grund: {reason}')
            embed2 = discord.Embed(color=0xE74C3C, title='Gebannt!', description=f'Du wurdest von **{guild.name}** gebannnt | Grund: **{reason}**')
            await member.send(embed=embed2)
            await member.ban(reason=reason)
            await ctx.reply(embed=embed1, mention_author=False)
        else:
            error = discord.Embed(color=0xE74C3C, title=f'Stop!', description=f'Du kannst {member.mention} nicht bannen! DU MONG DB')
            await ctx.send(embed=error)
            return
            
async def setup(client):
    await client.add_cog(Ban(client))