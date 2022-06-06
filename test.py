import discord
from discord.ext import commands

client = commands.Bot(command_prefix=';')

@client.command()
async def laurens(self, ctx):
    await ctx.reply('Hello there!')

client.run('')