import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        await ctx.reply('**Commands:**\n*Prefix:";"*\n  -help (show this list)\n  -gay (secret message)\n  -jasonisttoll (😳😳😳😳😳😳😳)\n  -clear [amount] (clear chat)\n  -8ball [question] (8ball command)\n  -ban [member] (ban command)\n  -kick [member] (kick command)\n  -load [command] (load command)\n  -unload [command] (unload command)\n*by Laurens*')

def setup(client):
    client.add_cog(Help(client))