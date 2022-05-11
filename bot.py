import random
import discord
import os
from discord.ext import commands

from commands.ball import Ball
from commands.ban import Ban
from commands.clear import Clear
from commands.error import CommandErrorHandler
from commands.gay import Gay
from commands.help import HelpCommand
from commands.jasonisttoll import Jason
from commands.kick import Kick
from commands.report import Report
  
client = commands.Bot(command_prefix=';', intents = discord.Intents.default(), help_command=commands.HelpCommand())
client.remove_command("help")

class HelpCmdLol(commands.HelpCommand):
  
  def __init__(self):
      super().__init__()
    
  async def send_bot_help(self, mapping):
    for cog in mapping:
      await self.get_destination().send(f'{cog.qualified_name}: {[command.name for command in mapping[cog]]}')

@client.event
async def on_ready():
  print('Bot ist gestartet!!!!!!!!')

@client.command()
async def unload(ctx, extension):
  if ctx.author.id == 712341730480881707:
    client.unload_extension(f'cogs.{extension}')
    await ctx.reply(f'**{extension} Cock** wurde entladen')

@client.command()
async def load(ctx, extension):
  if ctx.author.id == 712341730480881707:
    client.load_extension(f'commands.{extension}')
    await ctx.reply(f'**{extension} Cock** wurde geladen')

async def setup():
  await client.wait_until_ready()
  client.add_cog(Ball(client))
  client.add_cog(Ban(client))
  client.add_cog(Clear(client))
  client.add_cog(CommandErrorHandler(client))
  client.add_cog(Gay(client))
  client.add_cog(HelpCommand(client))
  client.add_cog(Jason(client))
  client.add_cog(Kick(client))
  client.add_cog(Report(client))

    
client.run('OTY4ODY0NDgxMDI1MzU5OTUy.YmlDXA.8RHND8yc6t607EVU_3KpVjN3StU')