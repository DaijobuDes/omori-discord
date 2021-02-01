import time
import datetime
import logging
import discord
import asyncio
import os

from discord.ext import commands
from colored_log import ColoredFormatter
from directinput import PressKey, ReleaseKey, Z, X, Q, W, LShift, UpArrow, DownArrow, LeftArrow, RightArrow

TOKEN = ""
log = logging.getLogger('omori')

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

cf = ColoredFormatter("[%(asctime)s][%(name)s][%(levelname)s] = %(message)s (%(filename)s:%(lineno)d)")

ch.setFormatter(cf)
log.addHandler(ch)

log.setLevel(logging.DEBUG)


client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    os.system('cls')
    username = client.user.name
    discriminator = client.user.discriminator
    log.debug('Client Online')
    log.debug('---------------------------------------------')
    log.debug(f'Client Name: {username}#{discriminator}')
    log.debug(f'Client ID: {str(client.user.id)}')
    log.debug(f'Discord.py Version: {discord.__version__}')
    log.debug('---------------------------------------------')

@client.event
async def on_message(message):
    if message.channel.id == None: # Enter channel ID to listen, must be an integer
        if message.content.lower() == 'up':
            PressKey(UpArrow)
            log.debug('up')
            await asyncio.sleep(0.1)
            ReleaseKey(UpArrow)

        if message.content.lower() == 'down':
            PressKey(DownArrow)
            log.debug('down')
            await asyncio.sleep(0.1)
            ReleaseKey(DownArrow)

        if message.content.lower() == 'left':
            PressKey(LeftArrow)
            log.debug('left')
            await asyncio.sleep(0.1)
            ReleaseKey(LeftArrow)

        if message.content.lower() == 'right':
            PressKey(RightArrow)
            log.debug('right')
            await asyncio.sleep(0.1)
            ReleaseKey(RightArrow)
            
        if message.content.lower().startswith('z'):
            PressKey(Z)
            log.debug('z')
            await asyncio.sleep(0.1)
            ReleaseKey(Z)

        if message.content.lower().startswith('x'):
            PressKey(X)
            log.debug('x')
            await asyncio.sleep(0.1)
            ReleaseKey(X)


        if message.content.lower().startswith('q'):
            PressKey(Q)
            log.debug('q')
            await asyncio.sleep(0.1)
            ReleaseKey(Q)

        if message.content.lower().startswith('w'):
            PressKey(W)
            log.debug('w')
            await asyncio.sleep(0.1)
            ReleaseKey(W)

        # Control running
        if message.content.lower().startswith('up!'):
            PressKey(LShift)
            PressKey(UpArrow)
            log.debug('run up')
            await asyncio.sleep(0.1)
            ReleaseKey(LShift)
            ReleaseKey(UpArrow)

        if message.content.lower().startswith('down!'):
            PressKey(LShift)
            PressKey(DownArrow)
            log.debug('run down')
            await asyncio.sleep(0.1)
            ReleaseKey(LShift)
            ReleaseKey(DownArrow)

        if message.content.lower().startswith('left!'):
            PressKey(LShift)
            PressKey(LeftArrow)
            log.debug('run left')
            await asyncio.sleep(0.1)
            ReleaseKey(LShift)
            ReleaseKey(LeftArrow)

        if message.content.lower().startswith('right!'):
            PressKey(LShift)
            PressKey(RightArrow)
            log.debug('run right')
            await asyncio.sleep(0.1)
            ReleaseKey(LShift)
            ReleaseKey(RightArrow)
        
        if message.content.lower().startswith('shift'):
            PressKey(LShift)
            log.debug('shift')
            await asyncio.sleep(0.1)
            ReleaseKey(LShift)

@client.command(name="ping")
async def ping(ctx):
    message = await ctx.send("pong")
    latency = round(client.latency*1000)
    log.debug(f'{ctx.message.author}: ping with latency of {latency} on {ctx.message.guild}.')
    await message.edit(content=f'{latency} ms')


client.run(TOKEN, reconnect=True)