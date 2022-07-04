import discord
from discord.ext import commands

class Del(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):

        all_bad_words = [
            
        ]
        luis_bad_words = [
            'Pay',
            'pAy',
            'paY',
            'PAy',
            'PaY',
            'pAY',
            'pay',
            'PAY',
            'cringe',
            'Cringe'
        ]

        msg = message.content
        if msg in all_bad_words:
            await message.delete()
        
        #if message.author.id == 400341760569507841:
        #    if msg in luis_bad_words:
        #        await message.delete()

async def setup(client):
    await client.add_cog(Del(client))
