from dislash import *
from discord.ext import commands
from discord import Embed, Status


class Server(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @slash_commands.command(
        name="server_info",
        description="View server information",
        guild_ids=[753623970863120434]
    )
    async def server_info(self, ctx):
        emb = Embed(title=f"Информация о сервер {ctx.guild.name}", color=0x0080ff)
        emb.set_thumbnail(url=ctx.guild.icon_url)

        ok = [
            {
                "name": f"Владелец сервера:",
                "value": ctx.guild.owner.mention
            },
            {
                "name": f"Сервер создан:",
                "value": f"{ctx.guild.created_at.strftime('%d.%m.%Y')}"
            },
            {
                "name": "Количество эмодзи:",
                "value": len(ctx.guild.emojis)
            },
            {
                "name": "Количество бустов",
                "value": ctx.guild.premium_subscription_count
            },
            {
                "name": f"Количество участников {ctx.guild.member_count}:",
                "value": "\n".join(
                    (
                        f"<:online:852663368418066473> Онлайн: {sum(i.status == Status.online for i in ctx.guild.members)}",
                        f"<:cpit:852665608751022090> Не активен: {sum(i.status == Status.idle for i in ctx.guild.members)}",
                        f"<:netrogay:852665562227802133> Не беспокоить: {sum(i.status == Status.dnd for i in ctx.guild.members)}",
                        f"<:offline:852665632302694401> Оффлайн: {sum(i.status == Status.offline for i in ctx.guild.members)}"
                    )
                )
            }
        ]

        for i in ok:
            emb.add_field(**i, inline=True)
        
        await ctx.send(embed=emb)


def setup(bot):
    bot.add_cog(Server(bot))