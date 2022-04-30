import discord
import os
from discord.ext import commands

class Report(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def report(self, ctx, member:discord.Member, *, report=None):
        report_channel = discord.utils.get(ctx.guild.channels, name = 'reports')
        if member is None:
            return await ctx.reply("Bitte sag wenn du Reporten möchtest.")
        if report is None:
            return await ctx.reply("Bitte erklär den grund für den Report.")
        else:
            embed = discord.Embed(title="Report", description=f"{ctx.author.mention} hat {member} Reportet", color=0xE74C3C)
            embed.set_thumbnail(url="")
            embed.add_field(name="Report grund:", value=f'{report}')
            embed.set_footer(text=f'Reagiere mit 😪 wenn die Situation sich gekläret hat. LOL.')
            report_message = await report_channel.send(embed=embed)
            await report_message.add_reaction('😪')
            await ctx.send(f'{ctx.author.mention} Dein Report wurde zu dem Team geschickt.')

            try:
                def check(reaction, user):
                    return user == ctx.author and str(reaction.emoji) in ['😪']
                
                reaction, user = await commands.wait_for('raction_add', timeout=604800, check=check)

                if str(reaction.emoji) == '😪':
                    await ctx.send(f'Der Report von {ctx.author.mention} hat sich geklärt.')
                    await print("HEHE")

            except Exception as e:
                print(e)
                    

def setup(client):
    client.add_cog(Report(client))