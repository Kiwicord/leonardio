import discord
from discord.ext import commands
import asyncio
import random
import datetime

class Giveaway(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def giveaway(self, ctx):
        
        giveaway_questions = ['Wo soll das Giveaway gestartet werden?', 'Was wird der Peris?', 'Wie lange soll das Giveaway gehen (in sekunden)?',]
        giveaway_answers = []

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        for question in giveaway_questions:
            await ctx.send(question)
            try:
                message = await self.client.wait_for('message', timeout= 30.0, check= check)
            except asyncio.TimeoutError:
                await ctx.send('Du hast nicht in der vorgegebennen Zeit(30 sekunden) geantwortet.')
                return
            else:
                giveaway_answers.append(message.content)

        try:
            c_id = int(giveaway_answers[0][2:-1])
        except:
            await ctx.send(f'You failed to mention the channel correctly.  Please do it like this: {ctx.channel.mention}')
            return

        channel = self.client.get_channel(c_id)
        prize = str(giveaway_answers[1])
        time = int(giveaway_answers[2])

        await ctx.send(f'Das giveaway für {prize} wird in kürze beginnen.\nBitte verfasse deine Teilnahme in {channel.mention}, dieses Giveaway wir in {time} sekunden enden.')

        give = discord.Embed(color = 0x2ecc71)
        give.set_author(name = f'GIVEAWAY TIME!', icon_url = 'https://i.imgur.com/VaX0pfM.png')
        give.add_field(name= f'{ctx.author.name} is giving away: {prize}!', value = f'React with 🎉 to enter!\n Ends in {round(time/60, 2)} minutes!', inline = False)
        end = datetime.datetime.utcnow() + datetime.timedelta(seconds = time)
        give.set_footer(text = f'Giveaway ends at {end} UTC!')
        my_message = await channel.send(embed = give)

        # Reacts to the message
        await my_message.add_reaction("🎉")
        await asyncio.sleep(time)

        new_message = await channel.fetch_message(my_message.id)

        # Picks a winner
        users = await new_message.reactions[0].users().flatten()
        users.pop(users.index(self.client.user))
        winner = random.choice(users)

        # Announces the winner
        winning_announcement = discord.Embed(color = 0xff2424)
        winning_announcement.set_author(name = f'THE GIVEAWAY HAS ENDED!', icon_url= 'https://i.imgur.com/DDric14.png')
        winning_announcement.add_field(name = f'🎉 Prize: {prize}', value = f'🥳 **Winner**: {winner.mention}\n 🎫 **Number of Entrants**: {len(users)}', inline = False)
        winning_announcement.set_footer(text = 'Thanks for entering!')
        await channel.send(embed = winning_announcement)

async def setup(client):
    await client.add_cog(Giveaway(client))