import discord
from discord.ext import commands

class Del(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        msg = message.content
        for word in msg:
            if msg.find('fuck') != -1:
                await message.delete()
                return 
            if msg.find('Fuck') != -1:
                await message.delete()
                return 
            if msg.find('Ficken') != -1:
                await message.delete()
                return 
            if msg.find('ficken') != -1:
                await message.delete()
                return 
            if msg.find('payday?') != -1:
                await message.delete()
                return
            if msg.find('Payday?') != -1:
                await message.delete()
                return
            if msg.find('payday') != -1:
                await message.delete()
                return
            if msg.find('Payday') != -1:
                await message.delete()
                return
            if msg.find('Pay Day?') != -1:
                await message.delete()
                return
            if msg.find('Pay day') != -1:
                await message.delete()
                return
            if msg.find('pay day?') != -1:
                await message.delete()
                return
            if msg.find('pay day') != -1:
                await message.delete()
                return
            if msg.find('PAYDAY') != -1:
                await message.delete()
                return
            if msg.find('PAY DAY') != -1:
                await message.delete()
                return
            if msg.find('uwu') != -1:
                await message.delete()
                return
            if msg.find('Uwu') != -1:
                await message.delete()
                return
            if msg.find('uWu') != -1:
                await message.delete()
                return
            if msg.find('uwU') != -1:
                await message.delete()
                return
            if msg.find('UWu') != -1:
                await message.delete()
                return
            if msg.find('UwU') != -1:
                await message.delete()
                return
            if msg.find('uWU') != -1:
                await message.delete()
                return
            if msg.find('UWU') != -1:
                await message.delete()
                return
            if msg.find('Amogus') != -1:
                await message.delete()
                return
            if msg.find('amogus') != -1:
                await message.delete()
                return
def setup(client):
    client.add_cog(Del(client))