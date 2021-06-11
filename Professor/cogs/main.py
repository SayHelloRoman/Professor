from dislash import *
from discord.ext import commands
from discord import Game


class mycog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_slash_command_error(self, ctx, ex):
        raise ex
    
    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity=discord.Game(name="https://github.com/SayHelloRoman/Professor"))


def setup(bot):
    bot.add_cog(mycog(bot))