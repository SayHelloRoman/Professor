from dislash import *
from discord.ext import commands


class mycog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_slash_command_error(self, ctx, ex):
        raise ex


def setup(bot):
    bot.add_cog(mycog(bot))