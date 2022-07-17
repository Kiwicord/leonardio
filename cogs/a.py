import discord
from discord.ext import commands

class A(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ass(self, ctx):
        if ctx.author == 977993035717681252:
            user = ctx.message.author
            role = discord.utils.get(user.server.roles, name="Blau")
            await user.add_roles(role)
        else:
            return
async def setup(client):
    await client.add_cog(A(client))