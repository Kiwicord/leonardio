import discord
from discord.ext import commands
import random

class Test(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def allah(self, ctx):
        print(f'{ctx.author.display_name} hat test ausgefürt.')
        while True:
            sus = [
             f'HEHEHEHA',
             f'DEIN E MOM',
             f'DU OPFER',
             f'FUCK U',
             f'SQUIDADEL SQUIDUDEL. UR DICK IS NOW A NUDEL',
             f'SCrrr Scrrr',
             f'freeeeeee freeeeeee',
             ]

            suss = random.choice(sus)

            embed = discord.Embed(title='', description=f'{suss}', color=0xE74C3C)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Test(client))