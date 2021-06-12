from dislash import *
from discord.ext import commands
from discord import Embed, Status


class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @slash_commands.command(
        name="ban",
        description="ban member",
        guild_ids=[753623970863120434],
        options=[
            Option("user", "user", Type.USER, required=True),
            Option("reason", "reason ban", Type.STRING)
        ]
        
    )
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx):
        user = ctx.get("user")
        reason = ctx.get("reason", "Фейс пам чел ты в бане")
        emb = Embed(title=f"{user} был забанен", color=0x0080ff)

        await user.ban(reason=reason)
        await ctx.send(embed=emb, delete_after=10)


def setup(bot):
    bot.add_cog(Ban(bot))