import discord
from discord.ext import commands

class Antrag(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def a(self, ctx, *, sus=None):
        if ctx.author.id == 745717254678904862 or 977993035717681252 or 941277767453016104:
            embed = discord.Embed(title= '**Abstimmung**', description= f'{ctx.author} möchte einen Abstimmung machen:', color=0xE74C3C)
            embed.add_field(name= 'Name:', value=f'{sus}')
            embed.add_field(name= 'Reagiere mit:', value= '✅ oder ❌')
            message = await ctx.send(embed=embed)
            await message.add_reaction('✅')
            await message.add_reaction('❌')

            def check(reaction, user):
                return str (reaction.emoji) == '❌' and user != self.client.user

            try:
                reaction, user = await self.client.wait_for('reaction_add', check=check)
                
                if str(reaction.emoji) == '❌':
                    while True:
                        await reaction.remove(user)
                return

            except Exception as e:
                print(e)

        else:
            await ctx.reply('LOL')
        print(f'{ctx.author.display_name} hat Antrag ausgefürt.')

async def setup(client):
    await client.add_cog(Antrag(client))