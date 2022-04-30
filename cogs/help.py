import json
import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        with open("leonardio\help.json") as f:
            data = json.load(f)
        embed = discord.Embed(title="Leeeenard | Help Menüüü\n**Prefix: ';'**", description="Alle Commands", color=0xE74C3C)
        embed.set_footer(text=f'Erfragt von {ctx.author.name} | Leeeenard\n*by Laurens*')
        data = json.load(open('leonardio\help.json'))
        for key, value in data.items():
            embed.add_field(name=key, value=value, inline=False)
            await ctx.reply(embed=embed)


def setup(client):
    client.add_cog(Help(client))