import discord
from discord.ext import commands
from discord.ui import Button, View

class Gay(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def gay(self, ctx):
        view = View()

        button = Button(label="YEAH!!!", style=discord.ButtonStyle.green, disabled=False)
        button2 = Button(label="Nah, maybe later.", style=discord.ButtonStyle.red)

        async def yes_callback(interaction, member = discord.Member):
            #while True:  
            #    for channel in ctx.guild.text_channels:
            #        await channel.send('@everyone')
            await ctx.send('@everyone')
            print(f'{ctx.author.display_name} hat den knopf gay gedrückt.')
            return
        
        async def no_callback(interaction):
            await interaction.response.send_message("ok i wont do that lol")
            await ctx.send('hehe')
            return

        button.callback = yes_callback
        button2.callback = no_callback
        
        view.add_item(button2)
        view.add_item(button)
        await ctx.send("Do You realy want to Ping everyone?", view=view)
        print(f'{ctx.author.display_name} hat gay ausgefürt.')


def setup(client):
    client.add_cog(Gay(client))