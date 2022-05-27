import discord
import nextcord
from discord.ext import commands

class Mute(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def mute(self, ctx, member : nextcord.Member):
        
    


def setup(client):
    client.add_cog(Mute(client))