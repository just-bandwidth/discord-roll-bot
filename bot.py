import random

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command(name="roll")
async def roll(ctx, minimum: int = 1, maximum: int = 100):
    """Roll a random number: !roll 1 100"""
    if minimum > maximum:
        minimum, maximum = maximum, minimum
    result = random.randint(minimum, maximum)
    await ctx.send(f"🎲 Rolled range {minimum}–{maximum}")
    await ctx.send(f"**{result}**")

@bot.event
async def on_ready():
    print(f"Bot online: {bot.user}")
