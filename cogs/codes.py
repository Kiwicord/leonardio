import random
import discord
from discord.ext import commands

class Codes(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def codes(self, ctx):
        print(f'{ctx.author.display_name} hat codes ausgefürt.')
        responses = [
        '253119',
        '289015',
        '261917',
        '364151',
        '375017',
        '375453',
        '372412',
        '377451',
        '379973',
        '378717',
        '354480',
        '296632',
        '235676',
        '191773',
        '76161',
        '350193',
        '361988',
        '27857',
        '126290',
        '344798',
        '397430',
        '347363',
        '313039',
        '370542',
        '162662',
        '218917',
        '195287',
        '330422',
        '274326',
        '368408',
        ]
        response = random.choice(responses)
        await ctx.reply(f'**Souce: {response}!**')

def setup(client):
    client.add_cog(Codes(client))