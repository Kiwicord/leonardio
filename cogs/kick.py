import discord
from discord.ext import commands

class Kick(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        if ctx.author.id == 745717254678904862:

            guild = ctx.guil
        
            await member.kick(reason=reason)
            await ctx.reply(f'{member.mention} wurde von diesem Server gekickt')
            await member.send(f'Du wurdest von **{guild.name}** geckickt | Grund: **{reason}**')

def setup(client):
    client.add_cog(Kick(client))