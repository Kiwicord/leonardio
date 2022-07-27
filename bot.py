import discord
from discord.ext import commands
from db import *
import asyncio
import os

PREFIX = ';'

client = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())
client.remove_command('help')

@client.event
async def on_ready():
  print('Finish\nLogged in as:\n{0.user.name}\n{0.user.id}'.format(client))
  act = discord.Activity(type=discord.ActivityType.playing, name='Deine Mutter Simulator 30001')
  await client.change_presence(activity=act)

@client.command()
async def load(ctx, extension):
    if ctx.author.id == 733403498766401554:
        client.load_extension(f'cogs.{extension}')

@client.command()   
async def unload(ctx, extension):
    if ctx.author.id == 733403498766401554:
        client.unload_extension(f'cogs.{extension}')

async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await client.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with client:
        await load_extensions()
        await client.start('OTc5MDE3NzAyOTU1OTUwMTYw.GqmYng.NhC_VKcZgu2RmV9Q1t5hPHvcjepFtWl26SqM1k')

asyncio.run(main())