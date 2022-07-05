import discord
from discord.ext import commands
import pyjokes as py

class Joke(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def joke(self, ctx):
            joke = py.get_joke()
            embed = discord.Embed(description=f'{joke}', color=0xE74C3C)
            embed.set_footer(text='Reagiere mit "⏯" für nächtsen Joke')
            message = await ctx.send(embed=embed)
            await message.add_reaction('⏯')

            def check(reaction, user):
                return str (reaction.emoji) == '⏯' and user != self.client.user
            try:
                reaction, user = await self.client.wait_for('reaction_add', check=check)

                if str(reaction.emoji) == '⏯':
                    await self.joke(ctx)
                    return   
                return

            except Exception as e:
                print(e)

    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def jokemany(self, ctx):
        while True:
            for channel in ctx.guild.text_channels:
                joke = py.get_joke()
                embed = discord.Embed(description=f'{joke}', color=0xE74C3C)
                embed.set_footer(text='HEHEHEHA')
                await channel.send(embed=embed)

async def setup(client):
    await client.add_cog(Joke(client))