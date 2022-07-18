import discord
from discord.ext import commands

class invits(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        links = [
            ".gg",
            ".invite"
        ]

        if any(word in message.content.lower() for word in links):
            await message.delete()
            await message.channel.send("Fais pas ta pub :rat:")

def setup(bot):
    bot.add_cog(invits(bot))
