import discord
import os
from discord.ext import commands

class Report(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['r'])
    async def report(self, ctx, member:discord.Member, *, report=None):
        guild = ctx.guild
        report_channel = discord.utils.get(ctx.guild.channels, name = 'reports')
        if member is None:
            return await ctx.reply("Bitte sag wenn du Reporten möchtest.")
        if report is None:
            return await ctx.reply("Bitte erklär den Grund für den Report.")
        else:
            embed = discord.Embed(title="Report", description=f"{ctx.author.mention} hat {member} Reportet", color=0xE74C3C)
            embed.set_thumbnail(url="")
            embed.add_field(name="Report grund:", value=f'{report}')
            embed.set_footer(text=f'Reagiere mit 😪 wenn die Situation sich gekläret hat. Reagiere mit ❌ wenn der User gebannt werden soll.')
            report_message = await report_channel.send(embed=embed)
            await report_message.add_reaction('😪')
            await report_message.add_reaction('❌')
            embed2 = discord.Embed(title='Report', description=f'{ctx.author.mention} Dein Report wurde zu dem Team geschickt.', color=0xE74C3C)
            embed5 = discord.Embed(title='Report', description=f'{member} wurde auf {guild.name} von {ctx.author.mention} wegen {report} Reportet.', color=0xE74C3C)
            await ctx.send(embed=embed2)
            await member.send(embed=embed5)

            def check(reaction, user):
                return user == ctx.author and (str(reaction.emoji) == '😪', '❌')
  
            try:
                reaction, user = await self.client.wait_for('reaction_add', check=check)
                if str(reaction.emoji) == '😪':
                    embed3 = discord.Embed(title='Report', description=f'Der Report von {ctx.author.mention} hat sich geklärt.', color=0xE74C3C)
                    embed4 = discord.Embed(title='Report', description=f'Der Report auf {guild.name} von {ctx.author.mention} über {member} hat sich geklärt.', color=0xE74C3C)
                if str(reaction.emoji) == '❌':
                    embed6 = discord.Embed(title='Report', description=f'{member} wurde von {ctx.author.mention} wegen {report} Gebannt.', color=0xE74C3C)
                    await member.send(embed=embed6)
                    await report_channel(embed=embed6)
                    await member.ban(reason=report)

                await report_channel.send(embed=embed3)
                await member.send(embed=embed4)

            except Exception as e:
                print(e)
        print(f'{ctx.author.display_name} hat report ausgefürt.')

async def setup(client):
    await client.add_cog(Report(client))