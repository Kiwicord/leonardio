import json
import discord
from discord.ext import commands

class Pancake(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='pancake')
    async def pancake(self, ctx):
        with open("pancake.json") as f:
            data = json.load(f)
        embed = discord.Embed(title="Pancake bether help | Help Menüüü\nPrefix: 'p!'", description="Alle Commands", color=0xE74C3C)
        embed.set_footer(text=f'Erfragt von {ctx.author.name} | Pancake')
        data = json.load(open('pancake.json'))
        for key, value in data.items():
            embed.add_field(name=key, value=value, inline=False)
        await ctx.reply(embed=embed)
        print(f'{ctx.author.display_name} hat pancake ausgefürt.')


async def setup(client):
    await client.add_cog(Pancake(client))