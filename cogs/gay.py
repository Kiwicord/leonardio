import discord
from discord.ext import commands
from discord.ui import Button, View

class Gay(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def gay(self, ctx):
        button = Button(label="YEAH!!!", style=discord.ButtonStyle.green)
        button2 = Button(label="Nah, maybe later.", style=discord.ButtonStyle.red)

        async def button_callback(interaction):
            await interaction.response.send_message("@everyone")

        button.callback = button_callback
        button2.callback = button_callback
        view = View()
        view.add_item(button2)
        await ctx.send("So you are gay?", view=view)
        view.add_item(button)
        await ctx.send("Do You realy want to Ping everyone?", view=view)


def setup(client):
    client.add_cog(Gay(client))