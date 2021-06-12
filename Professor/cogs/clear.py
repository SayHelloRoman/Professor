from dislash import *
from discord.ext import commands
from discord import Embed, Status


class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @slash_commands.command(
        name="clear",
        description="Clear chat",
        guild_ids=[753623970863120434],
        options=[
            Option("amount", "Amount message", Type.INTEGER, required=True)
        ]
        
    )
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx):
        amount = int(ctx.get("amount"))
        emb = Embed(title=f"Удалено {amount} сообщений", color=0x0080ff)

        await ctx.channel.purge(limit=amount)
        await ctx.send(embed=emb, delete_after=10)


def setup(bot):
    bot.add_cog(Clear(bot))