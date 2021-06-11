import os

from discord import Intents
from discord.ext import commands
from dislash import slash_commands
from boto.s3.connection import S3Connection


s3 = S3Connection(os.environ['S3_KEY'], os.environ['S3_SECRET'])
bot = commands.Bot(command_prefix="!", intents=Intents.all())
slash = slash_commands.SlashClient(bot)


for file_name in os.listdir("./cogs"):
    if file_name.endswith(".py"):
        bot.load_extension(f"cogs.{file_name[:-3]}")


bot.run(token)