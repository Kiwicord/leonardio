import random
import discord
import os
from discord.ext import commands
  
client = commands.Bot(command_prefix=';', intents=discord.Intents.default())
client.remove_command("help")

@client.event
async def on_ready():
  print('Bot ist gestartet')

@client.command()
async def unload(ctx, extension):
  if ctx.author.id == 712341730480881707:
    client.unload_extension(f'cogs.{extension}')
    await ctx.reply(f'**{extension} Cock** wurde entladen')

@client.command()
async def load(ctx, extension):
  if ctx.author.id == 712341730480881707:
    client.load_extension(f'cogs.{extension}')
    await ctx.reply(f'**{extension} Cock** wurde geladen')

for filename in os.listdir(".\cogs"):
    if filename.endswith(".py"):
      client.load_extension(f"cogs.{filename[:-3]}")
    
client.run('OTY4ODY0NDgxMDI1MzU5OTUy.YmlDXA.8RHND8yc6t607EVU_3KpVjN3StU')