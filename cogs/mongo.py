import discord
from discord.ext import commands
from db import *

class Mongo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['bal', 'Bal', 'Balance', 'BAL'])
    async def balance(self, ctx, member: discord.User=None):
        if member is None:
            member = ctx.author
            wallet = await get_wallet(ctx.author.id)
            bank = await get_profile(ctx.author.id)
        elif member is not None:
            await open_profile(member.id)
            wallet = await get_wallet(member.id)
            bank = await get_profile(member.id)

        embed = discord.Embed(color=0xE74C3C, title=f'✨🧨 Kontostand für {member}🧨✨')
        embed.add_field(name=f'Geld', value=f'**{wallet:,}**🧨')
        embed.add_field(name=f'Bank', value=f'**{bank:,}**🧨')

        await ctx.reply(embed=embed, mention_author=False)

def setup(client):
    client.add_cog(Mongo(client))