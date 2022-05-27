import discord 
from discord.ext import commands 

class Userinfo(commands.Cog):
    def init(self, client):
        self.client = client 

    @commands.command()
    async def userinfo(self, ctx, member:discord.Member=None):
        if member:
            embed1=discord.Embed(title=f"Userinfo für {member.display_name}", color=0x4a62d9)
            embed1.add_field(name="Name:", value=f"{member.mention}")
            embed1.add_field(name="Status:", value=f"{member.status}")
            embed1.add_field(name="Bot:", value=f'{("Ja" if member.bot else "Nein")}')
            embed1.add_field(name="Server beigetreten:", value=f"{member.joined_at}")
            embed1.add_field(name="Discord beigetreten:", value=f"{member.created_at}")
            embed1.add_field(name="Rollen:", value=f"{len(member.roles)-1}")
            await ctx.send(embed=embed1)

        else:
            embed2=discord.Embed(title=f"Userinfo für {ctx.author.display_name}", color=0x4a62d9)
            embed2.add_field(name="Name:", value=f"{ctx.author.mention}")
            embed2.add_field(name="Status:", value=f"{ctx.author.status}")
            embed2.add_field(name="Bot:", value=f'{("Ja" if ctx.author.bot else "Nein")}')
            embed2.add_field(name="Server beigetreten:", value=f"{ctx.author.joined_at}")
            embed2.add_field(name="Discord beigetreten:", value=f"{ctx.author.created_at}")
            embed2.add_field(name="Rollen:", value=f"{len(ctx.author.roles)-1}")
            await ctx.send(embed=embed2)
def setup(client):
    client.add_cog(Userinfo(client))