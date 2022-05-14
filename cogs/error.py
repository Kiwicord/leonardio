import discord
from discord.ext import commands

class CommandErrorHandler(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        embed = discord.Embed(title="Fehler!", color=0xE74C3C, description=f"```{error}```")
        embed.set_footer(text="Um den Fehler zu reporten, wende dich bitte an das Serverteam.")
        await ctx.send(embed=embed, mention_author=False)

def setup(client):
    client.add_cog(CommandErrorHandler(client)) 