import json
import discord
from discord.ext import commands

class HelpCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='help')
    async def help_cmd(self, ctx):
        with open("help.json") as f:
            data = json.load(f)
        embed = discord.Embed(title="Leeeenard | Help Menüüü\nPrefix: ';'", description="Alle Commands", color=0xE74C3C)
        embed.set_footer(text=f'Erfragt von {ctx.author.name} | Leeeenard')
        data = json.load(open('help.json'))
        for key, value in data.items():
            embed.add_field(name=key, value=value, inline=False)
        await ctx.reply(embed=embed)
        print(f'{ctx.author.display_name} hat help ausgefürt.')


def setup(client):
    client.add_cog(HelpCommand(client))