import random
import discord
from discord.ext import commands

class Ball(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        print(f'{ctx.author.display_name} hat 8ball ausgefürt.')
        responses = [
        'Jaaaa',
        'Neinmnm',
        'Maybe😳',
        'Not today',
        ]
        response = random.choice(responses)
        await ctx.reply(f'**Frage:  {question}?**\n**Antwort: {response}!**')

def setup(client):
    client.add_cog(Ball(client))