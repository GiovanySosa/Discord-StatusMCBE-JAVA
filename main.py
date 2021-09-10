import discord
import os
from dotenv import load_dotenv
from mcstats import mcstats

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')









bot.run(TOKEN)
