import discord
import os
from discord.ext import commands
import time
from db import *

time.sleep(0.2)
os.system('cls')


client = commands.Bot(command_prefix=';' , intents = discord.Intents.default(), help_command=commands.HelpCommand())
client.remove_command("help")

@client.event
async def on_ready():
  print('Finish\nLogged in as:\n{0.user.name}\n{0.user.id}'.format(client))
  act = discord.Activity(type=discord.ActivityType.playing, name='Deine Mutter Simulator 30001')
  await client.change_presence(activity=act)

@client.command()
async def unload(ctx, extension):
  print(f'{ctx.author.display_name} hat unload ausgefürt.')
  if ctx.author.id == 712341730480881707 or 745717254678904862:
    client.unload_extension(f'cogs.{extension}')
    await ctx.reply(f'**{extension} Cock** wurde entladen.')

@client.command()
async def load(ctx, extension):
  print(f'{ctx.author.display_name} hat load ausgefürt.')
  if ctx.author.id == 712341730480881707 or 745717254678904862:
    client.load_extension(f'cogs.{extension}')
    await ctx.reply(f'**{extension} Cock** wurde geladen.')

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
      client.load_extension(f"cogs.{filename[:-3]}")

client.run('OTc5MDE3NzAyOTU1OTUwMTYw.GqmYng.NhC_VKcZgu2RmV9Q1t5hPHvcjepFtWl26SqM1k')