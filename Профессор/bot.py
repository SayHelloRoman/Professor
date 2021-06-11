import json
import os

from discord import Intents
from discord.ext import commands
from dislash import slash_commands


bot = commands.Bot(command_prefix="!", intents=Intents.all())
slash = slash_commands.SlashClient(bot)


for file_name in os.listdir("./cogs"):
    if file_name.endswith(".py"):
        bot.load_extension(f"cogs.{file_name[:-3]}")


with open("data.json") as f:
    bot.run(json.load(f)["token"])
