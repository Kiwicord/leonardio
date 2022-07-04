import discord
from discord.ext import commands

class Bots(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def bots(self, ctx):
        print(f'{ctx.author.display_name} hat bots ausgefürt.')
        await ctx.send(embed = discord.Embed(title='', description=f'<@979017702955950160> ist auf **{(len(self.client.guilds))}** Server(n):', color=0xE74C3C))

        for server in self.client.guilds:
            await ctx.send(embed = discord.Embed(title='', description=f'```{server}```', color=0xE74C3C))

async def setup(client):
    await client.add_cog(Bots(client))