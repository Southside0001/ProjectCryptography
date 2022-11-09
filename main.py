# Imports
import os
import multiprocessing
import concurrent.futures
import platform
import Cryptodome
import nextcord
import base64 as b64
from Cryptodome.Hash import SHA3_256
from nextcord.ext import commands
from dotenv import load_dotenv


# Config intents
intents = nextcord.Intents.default()
intents.message_content = True

# Get processor core count
cores = multiprocessing.cpu_count()

# Load enviroment vars
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="c!", intents=intents)

print("Nextcord API Version (Latest):", nextcord.__version__)
print("PyCryptodomex API Version (Latest):", Cryptodome.__version__)
print("Processor cores used:", cores)
print("OS Version:", platform.version())
print("System:", platform.system())


def discordBot():
    @bot.command()
    async def hash(ctx, argv):
        argv = SHA3_256.new(data=ctx)
        argv.update()
        goober = b64.urlsafe_b64encode(argv)
        await ctx.send(goober)

    bot.run(TOKEN)


if __name__ == "__main__":
    discordBot()
    with concurrent.futures.ThreadPoolExecutor(
        max_workers=cores
    ) as executor:  # Threading
        executor.map(discordBot, range(cores))
