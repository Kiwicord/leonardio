import discord
from discord.ext import commands

class Ban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason='Kein Grund angegeben'):
        print(f'{ctx.author.display_name} hat ban ausgefürt.')

        guild = ctx.guild

        if member:
            embed1 = discord.Embed(color=0xE74C3C, title='Gebannt!', description=f'Der Member {member.mention} wurde von {ctx.author.mention} gebannt. Grund: {reason}')
            embed2 = discord.Embed(color=0xE74C3C, title='Gebannt!', description=f'Du wurdest von **{guild.name}** gebannnt | Grund: **{reason}**')
            await member.send(embed=embed2)
            await member.ban(reason=reason)
            await ctx.reply(embed=embed1, mention_author=False)
        else:
            error = discord.Embed(color=0xE74C3C, title=f'Stop!', description=f'Du kannst {member.mention} nicht bannen! DU MONG DB')
            await ctx.send(embed=error)
            return

    @commands.has_permissions(ban_members=True) 
    @commands.command()
    async def unban(self, ctx, *, member):
        print(f'{ctx.author.display_name} hat unban ausgefürt.')

        guild = ctx.guild

        if member:
            banned_users = await ctx.guild.bans()
            member_name, member_discriminator = member.split('#')

            for ban_entry in banned_users:
                user = ban_entry.user

                if (user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)
                    embed3 = discord.Embed(color=0xE74C3C, title='Entbannt!', description=f'Der Member {member.mention} wurde von {ctx.author.mention} entbannt.')
                    embed4 = discord.Embed(color=0xE74C3C, title='Entbannt!', description=f'Du wurdest von **{guild.name}** entbannt.')
                    await ctx.reply(embed=embed3)
                    await member.send(embed=embed4)
                    return


        else:
            error = discord.Embed(color=0xE74C3C, title=f'Stop!', description=f'Du kannst {member.mention} nicht entbannen! DU MONG DB')
            await ctx.send(embed=error)
            return

def setup(client):
    client.add_cog(Ban(client))