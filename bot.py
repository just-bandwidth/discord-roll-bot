import os
import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command(name="roll")
async def roll(ctx, minimum: int = 1, maximum: int = 100):
    """Roll a random number between minimum and maximum (default 1-100)"""
    if minimum > maximum:
        minimum, maximum = maximum, minimum
    result = random.randint(minimum, maximum)
    await ctx.send(f"🎲 Rolled a **{result}** ({minimum}–{maximum})")

@bot.event
async def on_ready():
    print(f"Bot is ready as {bot.user}")

if __name__ == "__main__":
    token = os.environ["DISCORD_TOKEN"]
    bot.run(token)
