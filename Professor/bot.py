import os

from discord import Intents
from discord.ext import commands
from dislash import slash_commands


bot = commands.Bot(command_prefix="!", intents=Intents.all())
slash = slash_commands.SlashClient(bot)


for file_name in os.listdir("./Professor/cogs"):
    if file_name.endswith(".py"):
        bot.load_extension(f"Professor.cogs.{file_name[:-3]}")


bot.run(TOKEN)