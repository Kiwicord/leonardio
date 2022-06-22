import json
import discord
from discord.ext import commands

class NiceThings(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='nice-things')
    async def nicethings(self, ctx):
        with open("nice-things.json") as f:
            data = json.load(f)
        embed = discord.Embed(title="Leeeenard | Help Menüüü\nPrefix: ';'", description="Nice Things:", color=0xE74C3C)
        embed.set_footer(text=f'Erfragt von {ctx.author.name} | Leeeenard')
        data = json.load(open('nice-things.json'))
        for key, value in data.items():
            embed.add_field(name=key, value=value, inline=False)
        await ctx.reply(embed=embed)
        print(f'{ctx.author.display_name} hat nicethings ausgefürt.')


def setup(client):
    client.add_cog(NiceThings(client))