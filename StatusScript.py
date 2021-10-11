import datetime
import discord
from discord.ext import commands
from discord.ext.commands.context import Context
from discord.utils import get
import asyncio
import random

intents = discord.Intents.default()
client = commands.Bot(
    command_prefix="*",
    help_command=None,
    intents=intents
)

@client.event
async def on_ready():
    print("He iniciado sesión!")
    client.loop.create_task(change_status())

async def change_status():
    while True:
        try:
            await client.change_presence(activity=discord.Activity(
                type=discord.ActivityType.playing,
                details="Developed by SelimGuu#2226",
                name="Developed by SelimGuu#2226",
                game="https://discord.gg/RVPfHKc6",
                state=discord.Status.online))
            await asyncio.sleep(10)
        except:
            pass

@client.command(
    name="ping",
    aliases=["p"],
    description="Sendet Servus"
)
async def ping(ctx: Context):
    await ctx.channel.send(f"Servus {ctx.author.mention}")




























client.run("ODI2NDg4MTczMTIyODEzOTc1.YGNNFw.XWfDQzz1oAMIFHJ8NjAIf-f-VW4")